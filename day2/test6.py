def calcBmi(h, w):  # 自訂義一個計算並列印 bmi 函式
    bmi = w / (h/100)**2
    print("bmi = %.2f" % bmi)


if __name__ == '__main__':  # python 的主程式寫法
    calcBmi(170, 60)
    calcBmi(160, 50)


