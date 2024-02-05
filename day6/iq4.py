'''
+-------------+
     IQ 圖
 上一頁  下一頁
+-------------+
'''

import tkinter as tk
from PIL import ImageTk, Image

def update_image(index):
    pass


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
    prev_button = tk.Button(root, text="上一題 ")
    prev_button.pack(side=tk.LEFT, padx=10, pady=10)
    next_button = tk.Button(root, text="下一題 ")
    next_button.pack(side=tk.RIGHT, padx=10, pady=10)

    # 顯示第一題的圖
    update_image(1)

    # 啟動視窗
    root.mainloop()



