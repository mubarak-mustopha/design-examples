import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc, tb):
        pass

    def elapsed(self):
        return time.time() - self.start_time

with Timer() as start:
    time.sleep(10)
    print(start.elapsed())