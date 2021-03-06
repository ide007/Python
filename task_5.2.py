import sys

num_gen = (num for num in range(1, int(input('введите число: ')) + 1, 2))
print(type(num_gen), sys.getsizeof(num_gen), '\n', *num_gen)
