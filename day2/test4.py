data = "身高=170,體重=60"
# 請算出 bmi = ?
array = data.split(",")
print(array[0], array[1])
h = array[0].split("=")
print(h, h[0], h[1])
w = array[1].split("=")
print(w, w[0], w[1])

height = int(h[1]) / 100
weight = int(w[1])
bmi = weight / height**2
print("%.2f" % bmi)
