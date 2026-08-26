import string

CHARS = string.ascii_letters + string.digits

class Tokenizer:
    def __init__(self):
        self._setup()

    def _setup(self):
        self.tokens = []
        self.current = ""

    def tok(self, pattern):
        index = 0
        while index < len(pattern):
            char = pattern[index]
            if char in CHARS:
                self.current += char
            elif char == "\\":
                index += 1
                self.current += pattern[index]
            elif char == "*":
                self._add("Any")
            elif char == "{":
                self._add("EitherStart")
            elif char == ",":
                self._add(None)
            elif char == "}":
                self._add("EitherEnd") 
            elif char == "[":
                self._add("SqEitherStart")
            elif char == "]":
                self._add("SqEitherEnd")
            else:
                raise NotImplementedError(f"Unknown token '{char}'")
            
            index += 1
        self._add(None)
        return self.tokens
    
    def _add(self, node):
        if self.current:
            self.tokens.append(['Lit', self.current])
            self.current = ""
        if node is not None:
            self.tokens.append([node])
