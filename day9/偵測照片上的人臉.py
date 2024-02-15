import cv2  # 匯入 opencv 資源

# 人臉哈爾特徵檔
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

# 讀取影像檔
frame = cv2.imread('sample_image/test.jpg')
# print(frame)
# 將彩色圖片轉灰階, 目的:增加處理的效率
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# print(gray)

# 偵測人臉, 得到臉部的(x, y, w, h)
faces = face_cascade.detectMultiScale(
    gray,  # 目標圖片
    scaleFactor=1.1,  # 檢測粒度(數字越小越精準(但速度慢), 反之數字越大越模糊(速度快))
    minNeighbors=5,  # 重複檢測次數(每個目標至少要檢測通過幾次才算成功，才被認定是 face)
    minSize=(30, 30),  # 搜尋比對最小尺寸
    flags=cv2.CASCADE_SCALE_IMAGE  # 比對類型: 影像
)

# 顯示圖片
cv2.imshow('My Image', gray)

# 在圖片上按下任意鍵離開
c = cv2.waitKey(0)



