# 讀取 student.txt 檔案內容
# 目的: 1.印出該班級學生國文平均
file = open('student.txt', 'r', encoding='UTF-8')
rows = file.readlines()

total_chinese_score = 0  # 存放國文累計總成績
count = 0                # 存放筆數(學生人數)
for row in rows[1:]:
    # '劉一 18 90' 變成 ['劉一', '18', '90']
    #                  0      1       2
    name, age, chinese_score = row.strip().split(" ")
    chinese_score = int(chinese_score)
    print(chinese_score)
    total_chinese_score += chinese_score  # 累計國文成績
    count += 1        # 累計人次
print('--------------------')
avg = total_chinese_score / count
print('平均國文成績:', avg)
