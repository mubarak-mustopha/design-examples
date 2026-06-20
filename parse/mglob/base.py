class Match:
    def __init__(self, rest):
        self.rest = rest if rest is not None else Null()

    def match(self, text, start=0):
        end = self._match(text, start)
        return end == len(text)
    
    def __eq__(self, other):
        return self.__class__ == other.__class__ and \
                    self.rest == self.rest

class Null(Match):
    def __init__(self):
        self.rest = None

    def _match(self, text, start):
        return start