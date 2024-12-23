from functools import lru_cache

@lru_cache(maxsize=None)
def fib_with_cache(n):
    i, j = 0, 1
    for _ in range(n):
        i, j = j, i + j
    return i

print(fib_with_cache(int(input())))