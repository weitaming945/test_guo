import json
dic='{"aa":null,"bb":"women","dd":[11,23,14]}'
res=json.loads(dic)
print(res)


# with open('json.json','r',encoding='utf-8') as f:
#     res =json.load(f)
# print(res)