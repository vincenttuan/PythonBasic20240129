'''
+-------------+
     IQ 圖
 上一頁  下一頁
+-------------+
'''

import tkinter as tk
from PIL import ImageTk, Image

def update_image(delta):
    global current_image
    current_image += delta
    print(current_image)
    # 確保 current_image 在合法的範圍(1~20)
    if current_image <= 0:
        current_image = 1
    elif current_image > total_images:
        current_image = total_images

    root.title('IQ 測驗 {}/{}'.format(current_image, total_images))
    image_path = '{}.png'.format(current_image)
    img = Image.open(image_path)  # 取得 image 圖像物件
    img = img.resize((950, 400))
    photo = ImageTk.PhotoImage(img)  # 轉成可以放在 tkinter 的資料類型
    image_label.config(image=photo)
    image_label.image = photo



if __name__ == '__main__':
    current_image = 1
    total_images = 20

    # 主視窗
    root = tk.Tk()
    root.title('IQ 測驗')

    # 存放 IQ 圖
    image_label = tk.Label(root)
    image_label.pack()

    # 建立按鈕
    prev_button = tk.Button(root, text="上一題", command=lambda: update_image(-1))
    prev_button.pack(side=tk.LEFT, padx=10, pady=10)
    next_button = tk.Button(root, text="下一題", command=lambda: update_image(1))
    next_button.pack(side=tk.RIGHT, padx=10, pady=10)

    # 顯示第一題的圖
    update_image(0)

    # 啟動視窗
    root.mainloop()



