import json

file = open("/datas/huangyijie/my_data/dailydialog/classification_test.jsonl", 'r', encoding='utf-8')
papers = []
for line in file.readlines():
    dic = json.loads(line)
    papers.append(dic)
i = 0
res = []
emo_label = ['other emotion','anger','disgust','fear','happiness','sadness','surprise']
j = 0
for item in papers:
    j = j+1
    print(j)
    dic = {}
    content = ''
    content = '下面我将给你一段对话历史，请你根据这段对话，预测回复者的情绪，注意，你并不知道回复者将要回复什么内容。你只需回答出情绪类别即可，情绪类别从'+str(emo_label)+'中选择。对话历史：'+ str(item["history"])
    dic['role'] = 'user'
    dic['content'] = content
    res.append(dic)
    dic = {}
    dic['role'] = 'assistant'
    dic['metadata'] = ''
    dic['content'] = str(item['emo_label'])
    res.append(dic)
    i=i+1
    if(i%4==0):
        content = "下面我将给你一段对话历史，请你根据这段对话，预测回复者的情绪，注意，你并不知道回复者将要回复什么内容。你只需回答出情绪类别即可，情绪类别从"+str(emo_label)+"中选择。对话历史："+ str(item["history"])
        i=0
        temp = res.pop()
        temp2 = res.pop()
        new_data = {}
        new_data['history'] = res
        res = []
        ans = temp["content"]
        prompt = temp2["content"]
        new_data['prompt'] = prompt
        new_data['emo_lable'] = ans
        with open("/datas/huangyijie/my_data/change_train.json/res.json", 'a') as f:
            json.dump(new_data, f, ensure_ascii=False)
            f.write('\n')





        
       

        



#[{'role': 'user', 'content': '下面我将给你一段对话历史，请你根据这段对话，预测回复者的情绪，注意，你并不知道回复者将要回复什么内容。你只需回答出情绪类别即可，情绪类别从+item["emo_candidate"]中选取。对话历史：+ item["history"]'}, {'role': 'assistant', 'metadata': '', 'content': 'item[emo_lable]'}]

#content = '下面我将给你一段对话历史，请你根据这段对话，预测回复者的情绪，注意，你并不知道回复者将要回复什么内容。你只需回答出情绪类别即可，情绪类别从'+item["emo_candidate"]+'中选择。对话历史：'+ item["history"]






[{'role': 'user', 'content': '你好'}, {'role': 'assistant', 'metadata': '', 'content': '你好👋！我是人工智能助手 ChatGLM3-6B，很高兴见到你，欢迎问我任何问题。'}, {'role': 'user', 'content': '晚上吃什么'}, {'role': 'assistant', 'metadata': '', 'content': '晚上吃些什么取决于您的口味和饮食习惯。这里有一些建议供您参考：\n\n1. 中餐：炒菜、煲汤、炖肉、炒饭、炒 面、小炒肉、宫保鸡丁等。\n2. 西餐：汉堡、披萨、意面、牛排、烤鱼、沙拉等。\n3. 日餐：寿司、刺身、天妇罗、拉面、日式炖菜 等。\n4. 韩餐：石锅拌饭、辣炒年糕、韩式炖鸡等。\n\n此外，您还可以选择外卖或外出就餐。建议根据您的需求和口味选择合适的餐厅。如果您对特定菜肴有特殊喜好，也可以告诉我，我会尽力为您推荐。'}]