# 變數的應用 BMI
w = 60  # 體重(kg)
h = 170  # 身高(cm)
h = h / 100  # 身高(cm) 轉 身高(m)
print(w, h)
bmi = w / h**2
print(bmi)
# 若只要印出小數點 1 位 ?
# 利用 % 進行格式化
print("%.1f" % bmi)
print("%.2f" % bmi)
print("身高: %.1f cm 體重: %.1f kg BMI: %.2f" % (h*100, w, bmi))

