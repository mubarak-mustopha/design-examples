from .either import Either
from .lit import Lit

def test_either_left_match():
    assert Either([Lit("a"), Lit("b")]).match("a")

def test_either_right_match():
    assert Either([Lit("a"), Lit("b")]).match("b")

def test_either_both_no_match():
    assert not Either([Lit("a"), Lit("b")]).match("ab")

def test_either_followed_by_lit_match():
    assert Either([Lit("vercel"), Lit("neon")], Lit(".com")).match("neon.com")

def test_either_followed_by_lit_no_match():
    assert not Either([Lit("vercel"), Lit("neon")], Lit(".com")).match("neon.dev")

def test_either_three_sub_patterns_match():
    assert Either([Lit("abc"), Lit("def"), Lit("ghk")], Lit(".dev")).match("ghk.dev")

def test_either_four_sub_patterns_no_match():
    assert not Either([Lit("abc"), Lit("def"), Lit("ghk"), Lit("ijk")], Lit(".dev")).match("lmn.dev")