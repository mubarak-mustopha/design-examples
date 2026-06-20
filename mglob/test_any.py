from .any import Any
from .lit import Lit

def test_any_matches_empty_string():
    assert Any().match("")

def test_any_matches_fullstring():
    assert Any().match("abcdx")

def test_any_matches_prefix():
    assert Any(Lit("yz")).match("xyz")

def test_any_matches_suffix():
    assert Lit("abc", Any()).match("abc.com")