from lit import Lit

def test_literal_entire_string_match():
    assert Lit("abc").match("abc")

def test_literal_substring_no_match():
    assert not Lit("ab").match("abc")

def test_literal_superstring_no_match():
    assert not Lit("abc").match("ab")

def test_literal_followed_by_literal_match():
    assert Lit("a", Lit("b")).match("ab")

def test_literal_followed_by_literal_no_match():
    assert not Lit("a", Lit("b")).match("ax")