import random
# 答案比對
# 標準答案 (1: 'F') -> 題號: 答案
ans = {1: 'F', 2: 'D', 3: 'B', 4: 'A', 5: 'E', 6: 'E', 7: 'B', 8: 'B', 9: 'F', 10: 'C',
       11: 'C', 12: 'F', 13: 'F', 14: 'B', 15: 'B', 16: 'C', 17: 'F', 18: 'E', 19: 'C', 20: 'A'}

# 使用者初始答案
user = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '',
       11: '', 12: '', 13: '', 14: '', 15: '', 16: '', 17: '', 18: '', 19: '', 20: ''}

# 初始化分數, 每一題答對的分數
score, point = 0, 9

# 使用者寫答案(1~20題)
user[1] = 'F'
user[2] = 'C'

# 模擬使用者寫答案(1~20題)
for i in range(1, 21):
    user[i] = random.choice(['A', 'B', 'C', 'D', 'E', 'F'])

print('標準答案:', ans)
print('學生答案:', user)
# 遍歷使用者的答案(question: 題號, user_answer: 答案
for question, user_answer in  user.items():
    # 檢查答案是否存在於標準答案中
    if question in ans and user_answer == ans[question]:
        # 答案正確,增加分數
        score += point

print(f'您的分數是: {score} 分')




