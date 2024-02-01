# 模擬連續搭電梯
import time
min = 1
max = 7
print("本大樓有 %d~%d 層" % (min, max))

current_floor = 1  # 目前電梯的所在位置
while True:
    target_floor = int(input('請輸入樓層(%d~%d)或輸入0 退出程式' % (min, max)))
    if target_floor == 0:
        print('感謝使用電梯模擬程式 !')
        break
    if min <= target_floor <= max:
        # 電梯運作邏輯
        pass
    else:
        print('樓層輸入錯誤, 請從新輸入')
        continue
    print("電梯已到達 %d 樓, 請出電梯" % target_floor)

