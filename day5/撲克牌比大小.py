# 比 7 大小
import random

# 定義每一張撲克牌的面(key) - 數組
poker = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4

# 定義每一張撲克牌的值(value) - 字典格式
card_values = {'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

# 我的錢包(一千元)
player_money = 1000
computer_money = 2000

if __name__ == '__main__':
    while True:
        # 檢查遊戲是否結束
        if player_money <= 0:
            print('您破產了 GG !')
            break
        elif computer_money <= 0:
            print('電腦破產了 GG ! 您贏了 讚~~ 👍👍')
            break



