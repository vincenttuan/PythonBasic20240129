# break 強制跳出迴圈
# continue 提早進行下一次的迴圈
import random

if __name__ == '__main__':
    while True:
        n = random.randint(1, 100)
        if n % 2 == 0:
            continue
        print(n)
        if n == 99:
            break
