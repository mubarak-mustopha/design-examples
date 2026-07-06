from mglob.any import Any
from mglob.either import Either
from mglob.lit import Lit
from mglob.base import Null

class Parser:
    def _parse(self, tokens):
        if not tokens:
            return Null()
        
        front, back = tokens[0], tokens[1:]
        if front[0] == 'Lit': func = self._parse_lit
        elif front[0] == 'Any': func = self._parse_any
        elif front[0] == 'EitherStart': func = self._parse_either
        else: raise NotImplementedError(f"Unknown token type '{front[0]}'")

        return func(front[1:], back)
        
    def _parse_lit(self, rest, back):
        return Lit(rest[0], self._parse(back))

    def _parse_any(self, rest, back):
        return Any(self._parse(back))

    def _parse_either(self, rest, back):
        children = []

        while back and back[0][0] == 'Lit':
            children.append(Lit(back[0][1]))
            back = back[1:]

        if not back or back[0][0] != 'EitherEnd':
            raise NotImplementedError('Invalid `Either` pattern.')

        return Either(children, self._parse(back[1:]))