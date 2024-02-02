import matplotlib.pyplot as plt
# 學生成績
# 繪圖需要安裝繪圖套件
# pip install matplotlib
students = {'John': 90, 'Mary': 85, 'Jack': 100, 'Rose': 45, 'Helen': 72}

if __name__ == '__main__':
     print(students)
     # 分離學生名稱與分數
     names = list(students.keys())
     scores = list(students.values())
     print(names)
     print(scores)

     # 創建長條圖
     # plt.bar(names, scores, color='skyblue')
     # 創建折線圖
     plt.plot(names, scores, 'o-', color='red')
     # 設定圖形標籤與標題
     plt.xlabel('student name')
     plt.ylabel('score')
     plt.title('student score chart')
     # 顯示圖形
     plt.show()