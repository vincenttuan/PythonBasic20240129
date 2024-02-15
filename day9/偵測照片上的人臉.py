import cv2  # 匯入 opencv 資源

# 人臉哈爾特徵檔
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

# 讀取影像檔
frame = cv2.imread('sample_image/test.jpg')
# print(frame)
# 將彩色圖片轉灰階, 目的:增加處理的效率
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
print(gray)

# 顯示圖片
cv2.imshow('My Image', gray)

# 在圖片上按下任意鍵離開
c = cv2.waitKey(0)



