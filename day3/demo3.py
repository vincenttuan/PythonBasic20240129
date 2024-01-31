# 電腦選號 4 星彩
# 0~9 隨機選出 4 個數字
import random

if __name__ == '__main__':
    count = 4
    while count > 0:
        n = random.randint(0, 9)
        print(n, end=' ')
        count = count - 1