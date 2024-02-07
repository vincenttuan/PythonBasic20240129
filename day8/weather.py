# 天氣查詢
# 網路位置: https://openweathermap.org/api
# 資料位置: https://api.openweathermap.org/data/2.5/weather?q={}&appid={}
city_name = 'taipei,TW'
key = 'a60f29f9b7623bf199279d78a529a2c0'  # 請用自己的 key
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
url = url.format(city_name, key)
print(url)


