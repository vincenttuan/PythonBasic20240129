def calcBmi(h, w):  # 自訂義一個計算並列印 bmi 函式
    bmi = w / (h/100)**2
    print("bmi = %.2f" % bmi)

def getBmi(h, w):
    bmi = w / (h/100)**2
    return bmi  # 將 bmi 回傳

def getResult(bmi):
    if bmi <= 18:
        return "過輕"
    elif bmi > 23:
        return "過重"
    else:
        return "正常"

def getBmiAndResult(h, w):
    bmi = getBmi(h, w)
    result = getResult(bmi)
    return bmi, result

if __name__ == '__main__':  # python 的主程式寫法
    calcBmi(170, 60)
    calcBmi(160, 50)

    bmi = getBmi(180, 85)
    print(bmi)

    bmi, result = getBmiAndResult(175, 43)
    print(bmi, result)

