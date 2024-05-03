import matplotlib.pyplot as plt

# 建立一個記憶體以存儲已經計算過的值
memo = {0: 0, 1: 1, 2: 1}

def fibonacci(n):
    # 檢查該值是否已經被計算過
    if n in memo:
        return memo[n]
    
    # 計算新的斐波那契數
    fib_n = fibonacci(n-1) + fibonacci(n-2)
    
    # 將計算結果存儲在備忘錄中
    memo[n] = fib_n
    
    return fib_n

# 從 F(5) 到 F(50)，每次 F(4) 被計算的次數即為 F(n-4)
def calculate_F4_calls():
    results = {}
    for i in range(5, 51):
        f4_calls = fibonacci(i - 4)
        results[i] = f4_calls
    return results

# 獲取結果
results = calculate_F4_calls()

# 打印結果
# for key, value in results.items():
#     print(f"F({key})時，F(4)被計算了 {value} 次")

# 繪製折線圖
n_values = list(range(5, 51))
f4_counts = list(results.values())

plt.figure(figsize=(12, 6))
plt.plot(n_values, f4_counts, marker='o', color='b', linestyle='-')
plt.title('Number of Times F(4) is Calculated in Recursive Fibonacci')
plt.xlabel('Fibonacci Number Index (F(n))')
plt.ylabel('Number of Calls to F(4)')
plt.grid(True)
plt.show()