class Lit:
    def __init__(self, chars, rest=None):
        self.chars = chars
        self.rest = rest

    def match(self, text, start=0):
        end = start + len(self.chars)
        if text[start: end] != self.chars:
            return False
        
        if self.rest is not None:
            return self.rest.match(text, end)
        
        return end == len(text)
