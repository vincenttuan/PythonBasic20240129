import requests
import json
import matplotlib.pyplot as plt

# 計算 youbike 的使用率
# 使用率 usage_rate = bemp/tot
# 請印出每一個站點的使用率(由大到小)
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
json_list = json.loads(requests.get(url).text)

# 為每一個站計算使用率之後並新增一個使用率屬性來存放
for youbike in json_list:
    youbike['usage_rate'] = float("%.2f" % (youbike['bemp']/youbike['tot'] * 100))

# 利用 sorted() 排序, 可以加入 reverse=True 參數 (由大到小)
sorted_json_list = sorted(json_list, key=lambda youbike: youbike['usage_rate'], reverse=True)

# enumerate(sorted_json_list) 可以取得序號
station_names = []  # 放置所有站名
usage_rates = []    # 放置所有使用率
for i, youbike in enumerate(sorted_json_list):
    sna = youbike['sna']
    usage_rate = youbike['usage_rate']
    print('%d %s 使用率 %.1f %%' % (i+1, sna, usage_rate))
    station_names.append(sna)
    usage_rates.append(usage_rate)

# 創建折線圖
plt.plot(station_names, usage_rates, 'o-', color='red')
# 設定圖形標籤與標題
plt.xlabel('station name')
plt.ylabel('usage_rate')
plt.title('station usage rate chart')
# 顯示圖形
plt.show()
