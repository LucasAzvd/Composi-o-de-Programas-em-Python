# -*- coding: utf8
from numba import jit
import concurrent.futures

@jit(nogil=True)
def cumsum(n: int):
    rv = 0
    for i in range(n):
        rv += i
    print(rv)
    return rv

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        data = [100000, 10000000, 1000000, 20000000]
        for _ in executor.map(cumsum, data):
            print(_)