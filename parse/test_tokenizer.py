from tokenizer import Tokenizer

def test_tok_empty_string():
    assert Tokenizer().tok("") == []

def test_tokenizer_with_lit_only():
    assert Tokenizer().tok("abc") == [['Lit', 'abc']]

def test_tokenizer_with_lit_and_any():
    assert Tokenizer().tok("test*") == [['Lit', 'test'], ['Any']]

def test_tokenizer_with_either():
    assert Tokenizer().tok("*{pdf,txt}") == [['Any'],['EitherStart'],['Lit', 'pdf'], ['Lit', 'txt'], ['EitherEnd']]

def test_tok_lit_dot_with_escape_character():
    assert Tokenizer().tok("wikipedia\\.{com,org}\\*") == [['Lit', 'wikipedia.'], ['EitherStart'], ['Lit', 'com'], ['Lit', 'org'], ['EitherEnd'], ['Lit', '*']]

def test_tok_lit_backslash_with_esc_character():
    assert Tokenizer().tok("\\\\") == [['Lit', '\\']]
