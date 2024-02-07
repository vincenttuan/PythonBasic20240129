import requests
import json
# 計算 youbike 的使用率
# 使用率 usage_rate = bemp/tot
# 請印出每一個站點的使用率(由大到小)
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
json_list = json.loads(requests.get(url).text)

