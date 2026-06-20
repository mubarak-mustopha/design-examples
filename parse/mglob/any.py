from .base import Match

class Any(Match):
    def __init__(self, rest=None):
        super().__init__(rest)

    def _match(self, text, start=0):    
        for i in range(start, len(text) + 1):
            end = self.rest._match(text, i)
            if end == len(text):
                return end
        
        return None