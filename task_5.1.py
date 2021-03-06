import sys


def nums_generator(max_num):
   for num in range(1, max_num + 1, 2):
       yield num


a = nums_generator(int(input('введите значение n: ')))
print(type(a), sys.getsizeof(a))
print(*a)
