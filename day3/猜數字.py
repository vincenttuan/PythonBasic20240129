# 1~9 猜數字
# 若猜得比答案大 -> 顯示猜太大的
# 若猜得比答案小 -> 顯示猜太小的

import random

if __name__ == '__main__':
    answer = random.randint(1, 9)
    count = 0  # 猜的次數
    while True:
        # 請玩家猜
        user_guess = int(input('玩家請在 1~9 猜一個數字:'))
        count = count + 1
        if user_guess > answer:
            print("猜大了")
        elif user_guess < answer:
            print("猜小了")
        else:
            print("恭喜答對了, 總共猜了 %d 次" % count)
            break
