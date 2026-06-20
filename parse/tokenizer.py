import string

CHARS = string.ascii_letters + string.digits

class Tokenizer:
    def __init__(self):
        self._setup()

    def _setup(self):
        self.tokens = []
        self.current = ""

    def tok(self, pattern):
        for char in pattern:
            if char in CHARS:
                self.current += char
            elif char == "*":
                self._add("Any")
            elif char == "{":
                self._add("EitherStart")
            elif char == ",":
                self._add(None)
            elif char == "}":
                self._add("EitherEnd") 
            else:
                raise NotImplementedError(f"Unknown token '{char}'")
        self._add(None)
        return self.tokens
    
    def _add(self, node):
        if self.current:
            self.tokens.append(['Lit', self.current])
            self.current = ""
        if node is not None:
            self.tokens.append([node])
