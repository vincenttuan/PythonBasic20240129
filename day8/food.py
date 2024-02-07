import requests
import json
# 資料來源: https://data.moa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx
# 請找出 "品名" 中含有 "池上" 字樣的不合格米

url = 'https://data.moa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
json_list = json.loads(requests.get(url).text)

keyword = '日本'
for item in json_list:
    if keyword in item['品名']:
        print(item['品名'], item['不合格原因'])

