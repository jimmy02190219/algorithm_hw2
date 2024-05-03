import matplotlib.pyplot as plt

# 費氏數列的 n 值和相應的執行時間
n_values = list(range(1, 53))
execution_times = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.01, 0.01, 0.01, 0.02, 0.04, 0.06, 0.10, 0.16, 0.25, 0.40, 0.65, 1.03, 1.67, 2.72, 4.37, 7.03, 11.36, 18.41, 29.78, 48.05, 77.82, 125.78, 203.52, 329.10, 532.47, 861.79, 1394.27, 2256.23, 3645.82, 5895.10, 9526.55, 15393.75]

# 繪製折線圖
plt.figure(figsize=(12, 6))
plt.plot(n_values, execution_times, marker='o')
plt.title('Execution Time of Fibonacci Numbers')
plt.xlabel('n-th Fibonacci Number')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()
