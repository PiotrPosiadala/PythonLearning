import functools
import time

@functools.lru_cache(maxsize=100)
def fib(n):
    
    if n <= 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
        
    return result


start = time.time()

for i in range(1, 35):
    print(fib(i))

stop = time.time()
print("Execution time = {}". format(stop-start))

print(fib.cache_info())