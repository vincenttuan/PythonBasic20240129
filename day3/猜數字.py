# 1~9 猜數字
# 若猜得比答案大 -> 顯示猜太大的
# 若猜得比答案小 -> 顯示猜太小的

import random

if __name__ == '__main__':
    answer = random.randint(1, 9)
    count = 0  # 猜的次數
    min = 1  # 預設最小值
    max = 9  # 預設最大值
    while True:
        # 請玩家猜
        user_guess = int(input('玩家請在 1~9 猜一個數字:'))
        # 判斷數字是否是在 1~9 的範圍內  ?
        if user_guess < 1 or user_guess > 9:
            print("數字範圍不正確, 請重猜~")
            continue
        count = count + 1
        if user_guess > answer:
            print("猜大了")
            max = user_guess - 1
        elif user_guess < answer:
            print("猜小了")
            min = user_guess + 1
        else:
            print("恭喜玩家答對了, 總共猜了 %d 次" % count)
            break
        # 請電腦猜
        pc_guess = random.randint(min, max)
        print('電腦 1~9 所猜的數字是 %d' % pc_guess)
        if pc_guess > answer:
            print("電腦猜大了")
        elif pc_guess < answer:
            print("電腦猜小了")
        else:
            print("電腦答對了, 玩家輸了")
            break
