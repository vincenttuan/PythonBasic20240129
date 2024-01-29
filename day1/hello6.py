# 整合應用-找零錢程式
# 買飲料一瓶 23 元, 付了 100 元, 請問要找幾元 ?
# 50 元要找幾個 ? 10 元要找幾個 ? 5 元要找幾個 ? 1 元要找幾個 ?
price = 23
pay = 100
exchange = pay - price  # 77
print(exchange)  # 77
fifty = exchange // 50  # 1
print("50元 %d 個" % fifty)
exchange = exchange - fifty * 50  # 剩下 27
print(exchange)  # 27
ten = exchange // 10  # 2
print("10元 %d 個" % ten)
exchange = exchange - ten * 10  # 剩下 7 元
print(exchange)  # 7
five = exchange // 5  # 1
print("5元 %d 個" % five)
exchange = exchange - five * 5  # 剩下 2 元
print(exchange)  # 2
one = exchange
print("1元 %d 個" % one)
