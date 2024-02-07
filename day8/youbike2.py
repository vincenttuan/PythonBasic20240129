import requests
import json
# 計算 youbike 的使用率
# 使用率 usage_rate = bemp/tot
# 請印出每一個站點的使用率
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
json_list = json.loads(requests.get(url).text)

for youbike in json_list:
    sna = youbike['sna']
    usage_rate = youbike['bemp']/youbike['tot']
    print('%s 使用率 %.1f %%' % (sna, usage_rate*100))

