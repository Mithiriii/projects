import time
import functools


@functools.lru_cache(maxsize=100)
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


start = time.time()
for i in range(1, 37):
    result = fib(i)
    print("Iteration:", i)
    print("Time:", time.time() - start)
    print("*" * 30)

print("Execution time:", time.time() - start)
#print(fib.cache_info())