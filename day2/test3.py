a = "100, 85, 70"
b = "90 90 95"
# 請問 a, b 二班哪一班成績較優 ?
a_scores = a.split(", ")
b_scores = b.split(" ")
print(a_scores, b_scores)
a_summary = int(a_scores[0]) + int(a_scores[1]) + int(a_scores[2])
b_summary = int(b_scores[0]) + int(b_scores[1]) + int(b_scores[2])
print(a_summary, b_summary)
# 成績判斷
if a_summary > b_summary:
    print("A 班較優")
elif a_summary < b_summary:
    print("B 班較優")
else:
    print("A B 二班成績一樣")
