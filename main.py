"""
Catalan
"""
import functools
import time

# import numpy as np


@functools.lru_cache(maxsize=1000)
def catalan_recursive(n: int):
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 5

    catalan = 0
    for k in range(n):
        catalan += catalan_recursive(k) * catalan_recursive(n - k - 1)

    return catalan


def recursive_definition(n):
    for i in range(n + 1):
        print(i, ":", catalan_recursive(i))


if __name__ == "__main__":
    start = time.time()
    recursive_definition(1000)
    print(time.time())
