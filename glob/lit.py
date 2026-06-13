from base import Match

class Lit(Match):
    def __init__(self, chars, rest=None):
        super().__init__(rest)
        self.chars = chars

    def _match(self, text, start=0):
        end = start + len(self.chars)
        if text[start: end] != self.chars:
            return None
        
        return self.rest._match(text, end)
