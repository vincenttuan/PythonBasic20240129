data = "100, 90, 83, 70, 60"
# 請幫我計算出總分與平均 ?
print(data)
scores = data.split(", ")
print(scores)
print(scores[0], type(scores[0]))
print(scores[1], type(scores[1]))
print(scores[2], type(scores[2]))
print(scores[3], type(scores[3]))
print(scores[4], type(scores[4]))
summary = int(scores[0]) + int(scores[1]) + int(scores[2]) + int(scores[3]) + int(scores[4])
print('總分:', summary)
average = summary / len(scores)
print('平均:', average)

