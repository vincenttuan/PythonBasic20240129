# 學生成績
# 繪圖需要安裝繪圖套件
# pip install matplotlib
students = {'劉一': 90, '陳二': 85, '張三': 100, '李四': 45, '王五': 72}

if __name__ == '__main__':
     print(students)
     # 分離學生名稱與分數
     names = list(students.keys())
     scores = list(students.values())
     print(names)
     print(scores)
