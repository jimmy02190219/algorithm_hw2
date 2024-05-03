import time
import matplotlib.pyplot as plt

def fibonacci(n, memo):
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        memo[n] = 1
        return 1
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]

def measure_fibonacci_performance():
    times = []
    for i in range(1, 101):
        start_time = time.time()
        memo = {}
        result = fibonacci(i, memo)
        end_time = time.time()
        execution_time = end_time - start_time
        times.append(execution_time)
        print(f"F({i}) = {result}, took {execution_time:.2f} seconds")
        if execution_time > 43200:  # 超過 12 小時則停止
            print(f"Computation too long, stopped at F({i})")
            break
    return times

def plot_times(times):
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, len(times)+1), times, marker='o')
    plt.title('Fibonacci Computation Time Using Dynamic Programming')
    plt.xlabel('n')
    plt.ylabel('Time in seconds')
    plt.grid(True)
    plt.show()

times = measure_fibonacci_performance()
plot_times(times)
