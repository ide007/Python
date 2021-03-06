import sys
from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]   # result = [23, 1, 3, 10, 4, 11]
# в лоб
start = perf_counter()
rezult = []

for i in src:
    if src.count(i) == 1:
        rezult.append(i)

print(sys.getsizeof(rezult), type(rezult), perf_counter() - start, '\n', rezult)

start = perf_counter()

rez = (i for i in src if src.count(i) == 1)
print(sys.getsizeof(rez), type(rez), perf_counter() - start, '\n', *rez)
