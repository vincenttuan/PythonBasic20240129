# 寫一支 python 程式
# 能將 http://192.168.1.85/python/iq/1.png ~ http://192.168.1.85/python/iq/20.png
# 所有圖形下載
import requests

def download_image(image_url, file_name):
    response = requests.get((image_url))
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
            #print('寫入 %s ok' % file_name)
            print('寫入 {} ok'.format(file_name))


if __name__ == '__main__':
    base_url = 'http://192.168.1.85/python/iq/{}.png'
    for i in range(1, 21):  # 1~20
        image_url = base_url.format(i)
        file_name = f'{i}.png'  # 等同 file_name = "{}.png".format(i)
        # print(image_url)
        download_image(image_url, file_name)

    print("Write OK !")
