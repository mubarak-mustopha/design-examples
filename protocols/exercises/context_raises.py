class ContextRaises:
    def __init__(self, err_type):
        self.err_type = err_type

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type == self.err_type:
            return True
        else:
            raise AssertionError(f"Failed to raise expected error")

with ContextRaises(IndexError):
    raise IndexError

with ContextRaises(StopIteration):
    raise StopIteration

with ContextRaises(ValueError):
    raise TypeError

with ContextRaises(IndexError):
    print("Not raising any error man.")