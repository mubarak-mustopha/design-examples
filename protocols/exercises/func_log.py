from datetime import datetime

def wrap_logger(filename):
    def logger(func):
        def _inner(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, "a") as file:
                file.write(f"{func.__name__} was called at {datetime.now()}\n")
            return result
        return _inner
    return logger

@wrap_logger("test_file.txt")
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

fib(3)