data1 = "170, 160.5, 180"  # 身高
data2 = "60, 45, 89.5"     # 體重
# 請將正常範圍的 18 < bmi <= 23 印出
h_array = data1.split(", ")
w_array = data2.split(", ")
print(h_array, w_array)
h1, h2, h3 = float(h_array[0]), float(h_array[1]), float(h_array[2])
print(h1, h2, h3)
w1, w2, w3 = float(w_array[0]), float(w_array[1]), float(w_array[2])
print(w1, w2, w3)



