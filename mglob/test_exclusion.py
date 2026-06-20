from .any import Any
from .exclusion import Not
from .lit import Lit
from .charsets import Range

def test_not_pass():
    assert Not(Lit("abc")).match("abcdef")

def test_not_fail():
    assert not Not(Lit("abc")).match("abc")

def test_not_pass2():
    assert Not(Range('a', 'Z', Any())).match('2HCl')