import matplotlib.pyplot as plt
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

     # 創建長條圖
     plt.bar(names, scores, color='skyblue')
     # 設定圖形標籤與標題
     plt.xlabel('學生名稱')
     plt.ylabel('分數')
     plt.title('學生成績圖表')
     # 顯示圖形
     plt.show()