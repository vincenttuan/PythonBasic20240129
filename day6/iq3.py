# 利用 tkinter 來顯示 GUI
# 利用 PIL 來顯示圖像
import tkinter as tk
from PIL import Image, ImageTk

def display_image():
    image_path = '1.png'
    img = Image.open(image_path)  # 取得 image 圖像物件
    img = img.resize((400, 300))
    photo = ImageTk.PhotoImage(img)  # 轉成可以放在 tkinter 的資料類型
    image_label.config(image=photo)
    image_label.image = photo


if __name__ == '__main__':
    # 建立主視窗
    root = tk.Tk()
    root.title("IQ Viewer")
    # 建立一個可以存放圖像的標籤(GUI 元素)
    image_label = tk.Label(root)
    image_label.pack()  # 放置 GUI 元素
    # 在啟動時顯示圖像
    display_image()
    # 啟動視窗循環
    root.mainloop()





