# 模擬連續搭電梯
import time
min = 1
max = 101
print("本大樓有 %d~%d 層" % (min, max))

current_floor = 1  # 目前電梯的所在位置
while True:
    target_floor = int(input('請輸入樓層(%d~%d)或輸入0 退出程式:' % (min, max)))
    if target_floor == 0:
        print('感謝使用電梯模擬程式 !')
        break
    if min <= target_floor <= max:
        # 電梯運作邏輯
        if target_floor > current_floor:
            direction = '上樓'
        elif target_floor < current_floor:
            direction = '下樓'
        else:
            continue

        while current_floor != target_floor:
            print("電梯 %s 當前樓層 %d 樓" % (direction, current_floor))
            diff = abs(current_floor - target_floor)
            if diff > 50:
                time.sleep(0.1)
            elif diff > 10:
                time.sleep(0.5)
            else:
                time.sleep(1)

            if direction == '上樓':
                current_floor += 1  # 每次加一
            else:
                current_floor -= 1  # 每次減一

    else:
        print('樓層輸入錯誤, 請從新輸入')
        continue
    print("電梯已到達 %d 樓, 請出電梯" % target_floor)

