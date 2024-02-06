# 讀取 student.txt 檔案內容
# 目的: 1.印出該班級年紀最大的學生名字
file = open('student.txt', 'r', encoding='UTF-8')
rows = file.readlines()

max_age_name = ''
max_age = 0

for row in rows[1:]:
    name, age, chinese_score, sex = row.strip().split(" ")
    age = int(age)
    # 替換法
    if age > max_age:
        max_age = age
        max_age_name = name

print('年齡最大:', max_age_name)
print('年齡:', max_age)

