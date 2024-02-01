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


