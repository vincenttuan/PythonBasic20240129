import requests

# 圖像 URL
image_url = 'http://192.168.1.85/python/iq/1.png'

# 使用 Get 請求來取得圖像資源
response = requests.get(image_url)

# 檢查請求是否成功 (請求成功 HTTP 的狀態碼得到 200)
if response.status_code == 200:
    # 打開一個文件寫入影像數據(二進位)
    with open('1.png', 'wb') as file:
        # 執行寫入動作
        file.write(response.content)
    print('寫入成功')
else:
    print('無此資料')

