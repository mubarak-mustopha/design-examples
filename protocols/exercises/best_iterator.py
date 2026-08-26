class BestIterator:
    def __init__(self, text):
        self._text = text[:]

    def __iter__(self):
        return BestCursor(self._text)

class BestCursor:
    def __init__(self, text):
        self._text = text[:]
        self._row = 0
        self._col = -1

    def __next__(self):
        self._advance()
        if self._row == len(self._text):
            raise StopIteration
        elif self._col < 0:
            return self.__next__()
        else:
            return self._text[self._row][self._col]

    def _advance(self):
        if self._row < len(self._text):
            self._col += 1
            if self._col == len(self._text[self._row]):
                self._col = -1
                self._row += 1


def gather(buffer):
    result = ""
    for char in buffer:
        result += char
    return result

def test_better_iterator():
    assert gather(BestIterator(["ab", "cd", "e"])) == "abcde"

def test_better_iterator_empty_string():
    buffer = BestIterator(["a", ""])
    assert gather(buffer) == "a"

    buffer = BestIterator(["a", "", "bc", "", "de"])
    assert gather(buffer) == "abcde"

    buffer = BestIterator(["", "", ""])
    assert gather(buffer) == ""

def test_better_iterator_nested_loop():
    buffer = BestIterator(["ab"])

    result = ""
    for outer in buffer:
        for inner in buffer:
            result += inner
            
    assert result == "abab"

# ["abc", "def", "hjk"] 