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
    # 洗牌
    random.shuffle(poker)
    while True:
        # 檢查遊戲是否結束
        if player_money <= 0:
            print('您破產了 GG !')
            break
        elif computer_money <= 0:
            print('電腦破產了 GG ! 您贏了 讚~~ 👍👍')
            break
        # 下注
        bet = int(input(f'您的資金: {player_money}, 電腦資金: {computer_money} 請下注:'))
        if bet > player_money:
            print('金額過大請重新下注~')
            continue
        # 選擇大小
        choice = int(input('請選擇比 7 大(1)還是比 7 小(2):'))
        if choice < 1 or choice > 2:
            print('選擇錯誤請重新選擇')
            continue
        # 玩家抽一張牌
        player_card = poker[0]
        player_value = card_values[player_card]
        # 將牌刪除
        poker.__delitem__(0)
        # 開牌
        print(f'玩家的牌: {player_card} 值: {player_value}')
        # 計算損益
        if (choice == 1 and player_value > 7) or (choice == 2 and player_value < 7):
            player_money += bet
            computer_money -= bet
            print(f'玩家贏 {bet} 元, 目前餘額: {player_money}')
        else:
            player_money -= bet
            computer_money += bet
            print(f'玩家輸 {bet} 元, 目前餘額: {player_money}')

    print("Game Over !")

