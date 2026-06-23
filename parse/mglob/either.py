from .base import Match

class Either(Match):
    def __init__(self, matcher_list, rest=None):
        super().__init__(rest)
        self.matcher_list = matcher_list

    def _match(self, text, start=0):
        for m in self.matcher_list:
            end = m._match(text, start)
            if end is not None:
                end = self.rest._match(text, end)
                if end == len(text):
                    return end

        return None
    
    def __eq__(self, other):
        return super().__eq__(other) and \
            self.matcher_list == other.matcher_list 