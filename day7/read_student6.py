# 讀取 student.txt 檔案內容
# 假設有效的國文成績是介於 0~100 之間, 及格分數必須 >= 60
# 目的: 1.印出該班級國文成績在及格中最低的學生名字與分數

file = open('student.txt', 'r', encoding='UTF-8')
rows = file.readlines()

min_chinese_name = ''
min_chinese_score = 100

for row in rows[1:]:
    name, age, chinese_score, sex = row.strip().split(' ')
    # 若分數不及格則不列入計算
    chinese_score = int(chinese_score)
    if chinese_score < 60:
        continue
    if chinese_score < min_chinese_score:
        min_chinese_name = name
        min_chinese_score = chinese_score

print(min_chinese_name, min_chinese_score)
