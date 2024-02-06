# 讀取 student.txt 檔案內容
# 目的: 可以印出學生資料
file = open('student.txt', 'r', encoding='UTF-8')
# 讀取整個檔案內容到數組(rows)中
rows = file.readlines()
print('資料列數:', len(rows))
print('第一列資料:', rows[0].strip())  # strip() 去除後面的換行符號與空白
print('第二列資料:', rows[1].strip())
print('第三列資料:', rows[2].strip())
print('最末筆資料:', rows[len(rows)-1].strip())
print('----------------------------')
# 利用 for 迴圈將所有學生資料印出
for row in rows:
    print(row.strip())
print('----------------------------')
for i in range(0, len(rows)):
    print(i, rows[i].strip())

