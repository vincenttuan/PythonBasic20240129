# 人機互動 input
# 使用者可以自行輸入身高與體重
# 並且可以判斷是否正常,過輕或過重
# 18 < bmi <= 23 正常, bmi <= 18 過輕, bmi > 23 過重
import math

h = float(input('請輸入身高(cm):'))
w = float(input('請輸入體重(kg):'))
print(h, w)
print(type(h), type(w))
bmi = w / math.pow(h/100, 2)  # w / (h/100)**2
print(bmi)

# 判斷 bmi
if bmi <= 18:
    print('過輕')
elif bmi > 23:
    print('過重')
else:
    print('正常')
