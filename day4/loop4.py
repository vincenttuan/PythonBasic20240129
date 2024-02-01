# 模擬點餐系統
import time

print('歡迎光臨線上點餐系統')

menu = {
    "1": {"name": "大麥克", "price": 70},
    "2": {"name": "麥香魚", "price": 50},
    "3": {"name": "雙層牛肉", "price": 40},
    "4": {"name": "可樂", "price": 20},
    "5": {"name": "薯條", "price": 30},
}

def show_menu():
    print("菜單選項")
    for key, item in menu.items():
        # print("%s. %s - $%d" % (key, item["name"], item["price"]))
        print(f'{key}. {item["name"]} - ${item["price"]}')

if __name__ == '__main__':
    show_menu()