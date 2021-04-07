from datetime import datetime as time


# you don't need arr, you need 2 strings
def timeit(func):
    def wrapper(arr):
        start = time.now()
        func(arr)
        print(func.__name__, ' => ', time.now() - start)

    return wrapper
