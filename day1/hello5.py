# 今有雞、兔同籠，上有三十五頭，下九十四足。問雞、兔各幾何？
total = 35
feet = 94
x = total * 2
rabbit = (feet - x) / (4-2)
chicken = total - rabbit
print("雞: %d, 兔: %d" % (chicken, rabbit))
