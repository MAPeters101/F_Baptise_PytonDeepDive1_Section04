print(type(100))

import sys

print(sys.getsizeof(0))
print(sys.getsizeof(1))
print(sys.getsizeof(2**1000))
print((160-24)*8)
print()

import time

def calc(a):
    for i in range(10_000_000):
        a * 2

start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(end-start)

start = time.perf_counter()
calc(2**100)
end = time.perf_counter()
print(end-start)

start = time.perf_counter()
calc(2**10_000)
end = time.perf_counter()
print(end-start)


