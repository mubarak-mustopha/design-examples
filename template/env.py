class Env:
    def __init__(self, initial: dict):
        self.stack = [initial.copy()]

    def push(self, frame: dict):
        self.stack.append(frame)

    def pop(self):
        return self.stack.pop()

    def find(self, name):
        for frame in reversed(self.stack):
            if name in frame:
                return frame[name]

        return None
