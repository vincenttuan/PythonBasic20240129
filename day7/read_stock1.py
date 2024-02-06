# yield 殖利率 > 7%
# PE 本益比 < 20
# PB 股價淨值比 < 1
file = open('stock.txt', 'r', encoding='UTF-8')
rows = file.readlines()

for row in rows[2:]:
    # 資料整理: 將 " 去除, 將 - 改成 -1
    row = row.strip().replace('"', '').replace('-', '-1')
    # 證券代號,證券名稱,殖利率(%),股利年度,本益比,股價淨值比,財報年/季
    #    0      1       2         3     4       5        6
    data = row.split(",")
    symbol = data[0]
    name = data[1]
    yield_r = float(data[2])
    pe = float(data[4])
    pb = float(data[5])
    print(data, symbol, name, yield_r, pe, pb)
