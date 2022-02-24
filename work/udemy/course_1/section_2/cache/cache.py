import time
import functools


@functools.lru_cache()
def factorial(n):

    time.sleep(0.1)
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


start = time.time()
for i in range(1,11):
    print('{}!={}'.format(i, factorial(i)))
stop = time.time()
print("Execution time", stop - start)

print(factorial.cache_info())