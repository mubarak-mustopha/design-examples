def wrap(func):
    def _inner(*args):
        print("before call")
        func(*args)
        print("before call")
    return _inner

@wrap
def original(message):
    print(f"original: {message}")

# print(original)
original("example")