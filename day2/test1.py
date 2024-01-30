words = "she sell sea shell on the sea shore"
print(words)
print(words.count('sea'))  # 有幾個 sea ?
print(words.find('shell'))  # shell 的位置 ?
print(words.find('happy'))  # happy 的位置 ?
print(len(words))  # 總共有多少字 ?
# 利用 split() 來進行切割
array = words.split(" ")
print(array)
print(array[0])
print(array[1])
print(len(array))

