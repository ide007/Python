from functools import wraps

def val_checker(l_func):
    def _val_checcker(func):
        def wrapper(number):
            if l_func(number):
                print(func(number))
            else:
                raise ValueError(f'Incorrect input number: {number}')
        return wrapper
    return _val_checcker


@val_checker(lambda n: n > 0)
def calc_cube(n):
    return n ** 3

try:
    test = calc_cube(-4)
except ValueError as error:
    print(error)
