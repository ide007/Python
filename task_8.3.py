from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        numbers = [num for num in (*args, *kwargs.values())]
        n = [f'{func.__name__}({num}: {type(num)}' for num in numbers]
        print(*n, *func(*args, **kwargs), sep='\n')
    return wrapper


@type_logger
def calc_cube(*a, **b):
    numbers = [num for num in (*a, *b.values()) if isinstance(num, int) or isinstance(num, float)]
    return [n ** 3 for n in numbers]


test = calc_cube(3, 15, 4.1, 23, )
print(calc_cube.__name__)
