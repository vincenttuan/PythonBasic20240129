import requests
import json
# 天氣查詢
# 網路位置: https://openweathermap.org/api
# 資料位置: https://api.openweathermap.org/data/2.5/weather?q={}&appid={}
city_name = 'taipei,TW'
key = 'a60f29f9b7623bf199279d78a529a2c0'  # 請用自己的 key
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
url = url.format(city_name, key)
print(url)

json_dict = json.loads(requests.get(url).text)
print(json_dict)

print('天氣狀況', json_dict['weather'][0]['main'])
print('天氣說明', json_dict['weather'][0]['description'])
print('現在氣溫 %.1f°C' % (float(json_dict['main']['temp'])-273.15))
print('體感溫度 %.1f°C' % (float(json_dict['main']['feels_like'])-273.15))
print('現在濕度', json_dict['main']['humidity'])
print('現在風速', json_dict['wind']['speed'])
print('雲層覆蓋', json_dict['clouds']['all'])
