import requests
import json
# 資料位置: https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json

url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
json_list = json.loads(requests.get(url).text)
print('資料筆數', len(json_list))
# print(json_list)

keyword = '忠孝東路四段'
for youbike in json_list:
    if keyword in youbike['sna']:
        print("站名 %s 總量 %d 可借 %d 可還 %d 更新時間 %s" % (youbike['sna'], youbike['tot'], youbike['sbi'], youbike['bemp'], youbike['updateTime']))


