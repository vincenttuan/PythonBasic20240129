# 讀取 student.txt 檔案內容
# 目的: 可以印出學生年齡與平均
file = open('student.txt', 'r', encoding='UTF-8')
rows = file.readlines()

total_age = 0  # 存放年齡總數
count = 0      # 存放筆數(學生人數)
for row in rows[1:]:
    # '劉一 18' 變成 ['劉一', '18']
    #                  0      1
    name, age = row.strip().split(" ")
    age = int(age)
    print(age)
    total_age += age  # 累計年齡
    count += 1        # 累計人次
print('--------------------')
avg = total_age / count
print('平均年齡:', avg)
