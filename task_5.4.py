import sys
from time import perf_counter

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print('&'*25, 'с помощью цикла for in', '&'*25)
start = perf_counter()
a = []

for i in range(1, len(src)):
    if src[i] > src[i - 1]:
        a.append(src[i])

print(a, 'время выполнения: ', perf_counter() - start)
print(type(a), sys.getsizeof(a))
print('&'*25, 'с помощью генератора', '&'*25)

start = perf_counter()
b = (src[i] for i in range(1, len(src)) if src[i-1] < src[i]) # list_comprehensions

print(*b, 'время выполнения: ', perf_counter() - start)
print(type(b), sys.getsizeof(b))
print(*b)
