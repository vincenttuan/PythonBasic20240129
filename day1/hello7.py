# 整合應用-找零錢程式
# 買飲料一瓶 23 元, 付了 100 元, 請問要找幾元 ?
# 50 元要找幾個 ? 10 元要找幾個 ? 5 元要找幾個 ? 1 元要找幾個 ?
price = 23
pay = 100
exchange = pay - price
print(exchange)           # 77
fifty = exchange // 50    # 77 // 50 = 1 個 50 元
exchange = exchange % 50  # 77 % 50 = 27
ten = exchange // 10      # 27 // 10 = 2 個 10 元
exchange = exchange % 10  # 27 % 10 = 7
five = exchange // 5      # 7 // 5 = 1 個 5 元
one = exchange % 5        # 7 % 5 = 2 個 1 元

print("50元: %d 個" % fifty)
print("10元: %d 個" % ten)
print("5元: %d 個" % five)
print("1元: %d 個" % one)
