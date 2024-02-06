# yield 殖利率 > 7%
# PE 本益比 < 20
# PB 股價淨值比 < 1
file = open('stock.txt', 'r', encoding='UTF-8')
rows = file.readlines()

for row in rows:
    print(row.strip())
