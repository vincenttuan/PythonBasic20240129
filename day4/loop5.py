import time

print('歡迎光臨線上飲料點餐系統')
# 飲品, 價格,
menu = {
    1: {"name": "珍珠奶茶", "price": 35},
    2: {"name": "檸檬紅茶", "price": 20},
    3: {"name": "冬瓜茶", "price": 40},
}
# 甜度 (0(無糖), 1(半糖), 2(全糖))
sugar_options = {
    0: "無糖", 1: "半糖", 2: "全糖"
}
# 冰塊 (0(去冰), 1(少冰), 2(正常冰))
ice_options = {
    0: "去冰", 1: "少冰", 2: "正常冰"
}

def show_menu():
    print('飲料單')
    for key, item in menu.items():
        print(f'{key}, {item["name"]} - ${item["price"]}')

# 偏好選擇
def get_preference(options, message):
    print(message)
    for key, item in options.items():
        print(f'{key}: {item}')
    choice = int(input('請選擇:'))
    if choice in options:
        return options[choice]

# 下單
def order():
    total_price = 0
    order_items = []
    # -------------------------------------------------------------------------
    while True:
        show_menu()
        choice = int(input('請輸入飲料編號:'))
        if choice in menu:
            drink_name = menu[choice]["name"]
            drink_price = menu[choice]["price"]
            sugar = get_preference(sugar_options, "請選擇甜度")
            ice = get_preference(ice_options, "請選擇冰塊量")
            total_price += drink_price
            print(f'您點了{drink_name} {sugar} {ice} ${drink_price}')
            # 加入到 order_items 中
            order_items.append((drink_name, sugar, ice, drink_price))
            choice = input('是否要繼續點餐(y/n)?').lower()  # lower() 強制轉小寫
            if choice != 'y':
                break
    #-------------------------------------------------------------------------
    print('點餐完畢 ! 您的點餐明細:')
    for drink_name, sugar, ice, drink_price in order_items:
        print(f'明細: {drink_name} {sugar} {ice} ${drink_price}')
    print(f'總金額: ${total_price}, 請至櫃台結帳, 謝謝光臨 !')

if __name__ == '__main__':
    order()
