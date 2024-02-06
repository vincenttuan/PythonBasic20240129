# 讀取 student.txt 檔案內容
# 目的: 1.印出該班級男學生國文平均與女學生國文平均
file = open('student.txt', 'r', encoding='UTF-8')
rows = file.readlines()

total_chinese_score = 0         # 不分男女: 存放國文累計總成績
count = 0                       # 不分男女: 存放筆數(學生人數)
total_male_chinese_score = 0    # 男學生: 存放國文累計總成績
male_count = 0                  # 男學生: 存放筆數(學生人數)
total_female_chinese_score = 0  # 女學生: 存放國文累計總成績
female_count = 0                # 女學生: 存放筆數(學生人數)

for row in rows[1:]:
    # '劉一 18 90 男' 變成 ['劉一', '18', '90', '男']
    #                       0      1     2     3
    name, age, chinese_score, sex = row.strip().split(" ")
    chinese_score = int(chinese_score)
    print(chinese_score)
    # 不分男女計算
    total_chinese_score += chinese_score  # 累計國文成績
    count += 1        # 累計人次
    # 判斷男女計算
    if sex == '男':
        total_male_chinese_score += chinese_score
        male_count += 1
    else:
        total_female_chinese_score += chinese_score
        female_count += 1

print('--------------------')
avg = total_chinese_score / count
male_avg = total_male_chinese_score / male_count
female_avg = total_female_chinese_score / female_count
print('全班平均國文成績:', avg)
print('男生平均國文成績:', male_avg)
print('女生平均國文成績:', female_avg)
