import time

def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def measure_fibonacci_performance():
    times = []
    max_n = 0
    for i in range(1, 101):
        start_time = time.time()
        try:
            # 設定計時器，超過 43200 秒（12 小時）則中斷
            result = fibonacci_recursive(i)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"F({i}) = {result}, took {execution_time:.2f} seconds")
            times.append(execution_time)
            max_n = i
        except Exception as e:
            print(f"Stopped at F({i}): {str(e)}")
            break
        if execution_time > 43200:  # 超過 12 小時則停止
            print(f"Computation too long, stopped at F({i})")
            break

    return times, max_n

times, max_n = measure_fibonacci_performance()
print(f"Maximum n computed within time limits: F({max_n})")
