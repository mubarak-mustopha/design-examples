from .charsets import Charset, Range
from .any import Any
from .lit import Lit
from .either import Either

def test_charset_match_first_char():
    assert Charset('aeiuo', Any()).match('anaconda')

def test_charset_vowel_no_match():
    assert not Charset('aeiou').match('b')

def test_charset_followed_by_any_match():
    assert Any(Charset('FAANG', Either([Lit('*'), Lit('**')]))).match('dummyFAA**')

def test_range_match_text_starting_with_capital():
    assert Range('A', 'Z', Any()).match("Yolo")

def test_range_text_ending_with_capital_no_match():
    assert not Any(Range('a', 'z')).match('AY')