import matplotlib.pyplot as plt

def fibonacci_memo_count(n, memo, count):
   if n in memo:
       return memo[n]

   if n == 1 or n == 2:
       return 1

   else:
       # 每次 n == 4 被呼叫時增加計數
       if n == 4:
           count['F(4)'] += 1

       memo[n] = fibonacci_memo_count(n - 1, memo, count) + fibonacci_memo_count(n - 2, memo, count)
       return memo[n]

# 測量從 F(5) 到 F(50) 每次計算中 F(4) 被計算的次數
def measure_fibonacci_performance_memo_count():
   counts = []
   x_values = []  # 添加 x 軸值的列表

   for i in range(5, 51):
       memo = {}
       count = {'F(4)': 0}
       fibonacci_memo_count(i, memo, count)
       counts.append(count['F(4)'])
       x_values.append(i)  # 添加 x 軸值

   return x_values, counts

# 實施測量
x_values, counts = measure_fibonacci_performance_memo_count()

# 繪製圖形
plt.plot(x_values, counts)
plt.xlabel('n')
plt.ylabel('F(4) Counts')
plt.title('Fibonacci F(4) Counts')
plt.show()