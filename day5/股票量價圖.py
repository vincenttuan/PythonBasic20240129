# 股票價量圖
import matplotlib.pyplot as plt
import random

range_size = 20
# 模擬股票日期
dates = [f'2024-1-{i+1}' for i in range(range_size)]
print(dates)
# 模擬收盤資料
prices = [random.randint(100, 130) for _ in range(range_size)]
print(prices)
# 模擬成交量資料
volumes = [random.randint(50000, 120000) for _ in range(range_size)]
print(volumes)

ax1 = plt.subplot()  # 子圖(價格圖)
ax2 = ax1.twinx()    # 子圖(成交量圖)
print(ax1, ax2)

# 子圖(價格圖)
ax1.set_xlabel('date')
ax1.set_ylabel('price', color='b')
ax1.plot(dates, prices, 'b-', label='price')
ax1.tick_params(axis='y', labelcolor='b')
ax1.legend(loc='upper left')

# 子圖(成交量圖)
ax2.set_xlabel('date')
ax2.set_ylabel('volume', color='g')
ax2.bar(dates, volumes, color='g', alpha=0.3, label='close')
ax2.tick_params(axis='y', labelcolor='g')
ax2.legend(loc='upper right')

# 設置 y 軸從 0 開始
ax1.set_ylim(0, max(prices) * 1.2)
ax2.set_ylim(0, max(volumes) * 2)

# 設置圖形標題
plt.title('stock chart')

# 顯示圖形
plt.show()

