import string

from .lit import Lit

CHARS = string.ascii_letters

class Charset(Lit):
    def _match(self, text, start):
        end = start + 1
        if text[start:end] in self.chars:
            return self.rest._match(text, end)
        return None

class Range(Charset):
    def __init__(self, first, last, rest=None):
        super().__init__(rest)
        start, end = CHARS.index(first), CHARS.index(last) + 1 
        chars = CHARS[start: end]
        super().__init__(chars, rest)
