import argparse
import re
import safetensors
from peft import PeftModel
from transformers import AutoConfig, AutoModel, AutoTokenizer
import torch
import os
import json

parser = argparse.ArgumentParser()

def refomat(response, emotion_map):
    pass


parser.add_argument("--model", type=str, default="/datas/huggingface/chatglm3-6b/", help="main model weights")
parser.add_argument("--tokenizer", type=str, default="/datas/huggingface/chatglm3-6b/", help="main model weights")
parser.add_argument("--lora-path", type=str, default="/datas/huangyijie/my_project/LLaMA-Factory/output")
parser.add_argument("--pt-pre-seq-len", type=int, default=256, help="The pre-seq-len used in p-tuning")
parser.add_argument("--device", type=str, default="cuda")
parser.add_argument("--max-new-tokens", type=int, default=2048)

args = parser.parse_args()

if args.tokenizer is None:
    args.tokenizer = args.model

if args.lora_path:
    tokenizer = AutoTokenizer.from_pretrained(args.tokenizer, trust_remote_code=True)
    config = AutoConfig.from_pretrained(args.model, trust_remote_code=True, pre_seq_len=args.pt_pre_seq_len)
    model = AutoModel.from_pretrained(args.model, config=config, trust_remote_code=True).cuda()
    model = PeftModel.from_pretrained(model, args.lora_path)
else:
    tokenizer = AutoTokenizer.from_pretrained(args.tokenizer, trust_remote_code=True)
    model = AutoModel.from_pretrained(args.model, trust_remote_code=True)

model = model.to(args.device)
# history = []
# while True:

#     prompt = input("Prompt:")
#     # inputs = tokenizer(prompt, return_tensors="pt")
#     # inputs = inputs.to(args.device)
#     # response = model.generate(input_ids=inputs["input_ids"], max_length=inputs["input_ids"].shape[-1] + args.max_new_tokens)
#     # response = response[0, inputs["input_ids"].shape[-1]:]
#     # print("Response:", tokenizer.decode(response, skip_special_tokens=True))
#     response, history = model.chat(tokenizer, prompt, history=history, max_length = args.max_new_tokens)
#     print(history)
#     result = refomat(response)
#     print("Response:", response)


file = open("/datas/huangyijie/my_data/change_train.json/res.json", 'r', encoding='utf-8')
papers = []
j = 0
for line in file.readlines():
    j = j+1
    dic = json.loads(line)
    history = dic["history"]
    prompt = dic["prompt"]
    response, history = model.chat(tokenizer, prompt, history=history, max_length = args.max_new_tokens)
    print("Response:", response)
    if(j==30):
        break


