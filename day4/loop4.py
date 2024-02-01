# 模擬點餐系統
import time

print('歡迎光臨線上點餐系統')

menu = {
    1: {"name": "大麥克", "price": 70},
    2: {"name": "麥香魚", "price": 50},
    3: {"name": "雙層牛肉", "price": 40},
    4: {"name": "可樂", "price": 20},
    5: {"name": "薯條", "price": 30},
}

def show_menu():
    print("菜單選項")
    for key, item in menu.items():
        # print("%s. %s - $%d" % (key, item["name"], item["price"]))
        print(f'{key}. {item["name"]} - ${item["price"]}')


def order():
    total_price = 0
    # -------------------------------------------------------------------------------
    while True:
        show_menu()
        choice = int(input('請輸入餐點號碼(輸入0結束點餐):'))
        if choice == 0:
            break
        if choice in menu:  # choice 是在 menu 中所定義的 key, 也就是 1, 2, 3, 4, 或 5
            item_name = menu[choice]["name"]
            item_price = menu[choice]["price"]
            total_price += item_price  # total_price = total_price + item_price
            print(f'您點了{item_name} 單價 ${item_price} 累計金額 ${total_price}')
            time.sleep(1)  # 模擬處理時間
            choice = input('是否要繼續點餐(y/n)?')
            if choice == 'n':
                break
        else:
            print('無此餐點, 請重新輸入')
            continue
    #-------------------------------------------------------------------------------
    print(f'點餐完畢, 總金額為: ${total_price} 請至櫃台結帳, 謝謝光臨 !')

if __name__ == '__main__':
    order()
    #print(menu.items())  # 會包含 key + item(value)
    #print(menu.values())  # 只會有 item(value), 但是沒有 key

