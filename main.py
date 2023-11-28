"""
Catalan
"""
import functools
import time
import numpy as np


@functools.lru_cache()
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

    catalan = [0 for i in range(n + 1)]

    catalan[0] = 1
    catalan[1] = 1
    for i in range(2, n + 1):
        for k in range(i):
            catalan[i] += catalan_recursive(i - k - 1) * catalan_recursive(k)

    return catalan[n]


def recursive_definition(n):
    for i in range(n + 1):
        print(i, ":", catalan_recursive(i))


if __name__ == "__main__":
    # import dis

    # dis.dis(catalan_recursive)
    start = time.time()
    recursive_definition(50)
    print(time.time())
