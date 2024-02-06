# yield 殖利率 > 7%
# PE 本益比 < 20
# PB 股價淨值比 < 1
file = open('stock.txt', 'r', encoding='UTF-8')
rows = file.readlines()

for row in rows:
    # 資料整理: 將 " 去除, 將 - 改成 -1
    row = row.strip().replace('"', '').replace('-', '-1')
    print(row)
