# 寫一支 python 程式
# 能將 http://192.168.1.85/python/iq/1.png ~ http://192.168.1.85/python/iq/20.png
# 所有圖形下載

def download_image(image_url, file_name):
    pass


if __name__ == '__main__':
    base_url = 'http://192.168.1.85/python/iq/{}.png'
    for i in range(1, 21):  # 1~20
        image_url = base_url.format(i)
        print(image_url)
