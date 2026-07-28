import pytest

class BetterIterator:
    def __init__(self, text):
        self._text = text[:]

    def __iter__(self):
        return BetterCursor(self._text)

class BetterCursor:
    def __init__(self, text):
        self._text = text
        self._row = 0
        self._col = -1

    def __next__(self):
        self._advance()
        if self._row == len(self._text):
            raise StopIteration
        return self._text[self._row][self._col]

    def _advance(self):
        if self._row < len(self._text):
            self._col += 1
            if self._col == len(self._text[self._row]):
                self._row += 1
                self._col = 0

def gather(buffer):
    result = ""
    for char in buffer:
        result += char
    return result

def test_naive_buffer():
    buffer = BetterIterator(["ab", "c"])
    assert gather(buffer) == "abc"

def test_naive_buffer_empty_string():
    buffer = BetterIterator(["a", ""])
    with pytest.raises(IndexError):
        assert gather(buffer) == "a"

def test_naive_buffer_nested_loop():
    buffer = BetterIterator(["a", "b"])
    result = ""

    for outer in buffer:
        for inner in buffer:
            result += inner
    assert result == "abab"