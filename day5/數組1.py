# 數組
# []     -> List 列表陣列, 元素內容可以重複
# set()  -> Set 列表陣列, 元素內容不可以重複
# dict() -> 字典格式 (key/value), key 不可重複, value 可以重複
a = [1, 3, 5, 7, 5]
print(a)
a[1] = 2  # 變更元素內容
print(a)
a.append(9)  # 增加元素
print(a)
a.remove(5)  # 移除元素內容 = 5 的資料 (一次只會移除一個)
print(a)
a.__delitem__(0)  # 移除指定位置的元素
print(a)
a.sort()  # 資料排序(小->大)
print(a)
a.reverse()  # 資料反轉
print(a)
print("最大值:", max(a))
print("最小值:", min(a))
