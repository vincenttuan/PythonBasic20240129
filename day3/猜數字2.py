# 猜數字 1~99 區間提示版
import random

if __name__ == '__main__':
    answer = random.randint(1, 99)
    min = 1
    max = 99
    while True:
        # 玩家猜
        user_guess = int(input('請在 %d ~ %d 猜一數字:' % (min, max)))
        # 判斷數字範圍
        if user_guess < min or user_guess > max:
            print('數字範圍錯誤, 請重猜~')
            continue
        # 判斷是否猜對 ?
        if user_guess > answer:
            max = user_guess - 1
        elif user_guess < answer:
            min = user_guess + 1
        else:
            print("玩家答對了, 答案是: %d" % answer)
            break

