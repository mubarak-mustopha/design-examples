from .base import Match

class Not(Match):
    def _match(self, text, start):
        end = self.rest._match(text, start)
        return None if end == len(text) else len(text)
    