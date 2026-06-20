from .base import Match

class Either(Match):
    def __init__(self, left, right, rest=None):
        super().__init__(rest)
        self.left = left
        self.right = right

    def _match(self, text, start=0):
        for m in [self.left, self.right]:
            end = m._match(text, start)
            if end is not None:
                end = self.rest._match(text, end)
                if end == len(text):
                    return end

        return None
    
    def __eq__(self, other):
        return super().__eq__(other) and \
            self.left == other.left and self.right == other.right