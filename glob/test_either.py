from either import Either
from lit import Lit

def test_either_left_match():
    assert Either(Lit("a"), Lit("b")).match("a")

def test_either_right_match():
    assert Either(Lit("a"), Lit("b")).match("b")

def test_either_both_no_match():
    assert not Either(Lit("a"), Lit("b")).match("ab")

def test_either_followed_by_lit_match():
    assert Either(Lit("vercel"), Lit("neon"), Lit(".com")).match("neon.com")

def test_either_followed_by_lit_no_match():
    assert not Either(Lit("vercel"), Lit("neon"), Lit(".com")).match("neon.dev")