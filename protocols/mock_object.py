class Fake:
    def __init__(self, func=None, value=None):
        self.calls = []
        self.func = func
        self.value = value

    def __call__(self, *args, **kwargs):
        self.calls.append([args, kwargs])
        if self.func is not None:
            return self.func(*args, **kwargs)
        return self.value

def fakeit(name, func=None, value=None):
    assert name in globals()
    fake = Fake(func, value)
    globals()[name] = fake
    return fake

def adder(a, b):
    return a + b

def test_with_real_function():
    assert adder(2, 3) == 5

def test_with_fixed_return_value():
    fakeit("adder", value=99)
    assert adder(2, 3) == 99

def test_fake_records_calls():
    fake = fakeit("adder", value=99)
    assert adder(2, 3) == 99
    assert adder(3, 4) == 99
    assert adder.calls == [[(2,3), {}], [(3,4), {}]]

def test_fake_calculates_result():
    fakeit("adder", func=lambda left, right: 10 * left + right)
    assert adder(2, 3) == 23

if __name__=="__main__":
    tests = [value for name, value in globals().items() if name.startswith("test")]
    for test in tests:
        print(f"running {test.__name__}")
        test()