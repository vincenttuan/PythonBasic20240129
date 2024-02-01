# 利用 for-loop 模擬搭電梯
import time

print("本棟大樓有1~7層")
target_floor = int(input('請輸入樓層:'))
for floor in range(1, 8):
    print('電梯上樓', floor)
    time.sleep(1)
    if floor == target_floor:
        print('電梯到達指定樓層, 請出電梯')
        break





