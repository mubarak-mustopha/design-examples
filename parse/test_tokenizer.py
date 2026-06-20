from tokenizer import Tokenizer

def tok_empty_string():
    assert Tokenizer().tok("") == []

def test_tokenizer_with_lit_only():
    assert Tokenizer().tok("abc") == [['Lit', 'abc']]

def test_tokenizer_with_lit_and_any():
    assert Tokenizer().tok("test*") == [['Lit', 'test'], ['Any']]

def test_tokenizer_with_either():
    assert Tokenizer().tok("*{pdf,txt}") == [['Any'],['EitherStart'],['Lit', 'pdf'], ['Lit', 'txt'], ['EitherEnd']]