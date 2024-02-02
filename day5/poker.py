# 數組與撲克牌
import random

# 定義每一張撲克牌的面(key) - 數組
poker = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4

# 定義每一張撲克牌的值(value) - 字典格式
card_values = {'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

if __name__ == '__main__':
    print(poker)
    # 利用 random 來洗牌
    random.shuffle(poker)
    print(poker)
    card1 = poker[0]
    card2 = poker[1]
    print("cart1:", card1)
    print("cart2:", card2)
    # 比較大小
    print("cart1 value:",  card_values[card1])
    print("cart2 value:", card_values[card2])
    if card_values[card1] > card_values[card2] :
        print("cart1 大")
    elif card_values[card1] < card_values[card2] :
        print("cart2 大")
    else:
        print("cart 1 cart2 一樣大")
