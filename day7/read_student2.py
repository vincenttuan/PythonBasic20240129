# 讀取 student.txt 檔案內容
# 目的: 可以印出學生年齡與平均
file = open('student.txt', 'r', encoding='UTF-8')
rows = file.readlines()
for row in rows[1:]:
    # '劉一 18' 變成 ['劉一', '18']
    #                  0      1
    data = row.strip().split(" ")
    print(data[1])
