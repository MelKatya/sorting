from functools import wraps
import time


def timer(func):
    """Декоратор для расчета времени выполнения функции"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = round(end_time - start_time, 6)
        print('Время выполнения функции "{func}" составляет {time} секунд'.format(
            func=func.__name__,
            time=total_time
        ))
        return result
    return wrapper
