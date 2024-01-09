import json

file = open("./train_3.5M_CN.json", 'r', encoding='utf-8')
file2 = open("reformat_llama_data_10K.jsonl", 'a', encoding='utf-8')
num = 0
for line in file.readlines():
    line = json.loads(line)
    dic = {}
    history = []
    turn = []
    for item in line["conversations"]:
        if item["from"] == "human" and len(turn) == 0:
            turn.append(item["value"])
        elif item["from"] == "assistant" and len(turn) == 1:
            turn.append(item["value"])
            history.append(turn)
            turn = []
        else:
            print("ERROR")
            break
    dic["instruction"] = history[-1][0]
    dic["input"] = ""
    dic["output"] = history[-1][1]
    history.pop()
    dic["history"] = history
    dic["system"] = "我是一个人工智能助手，我会一局指令完成任务"
    json.dump(dic, file2, ensure_ascii=False)
    file2.write('\n')
    if num == 10000:
        break
    else:
        num += 1
