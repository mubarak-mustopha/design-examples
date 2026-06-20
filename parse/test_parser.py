from mglob.any import Any
from mglob.either import Either
from mglob.lit import Lit
from mglob.base import Null

from parser import Parser
from tokenizer import Tokenizer

def test_parse_empty_string():
    assert Parser()._parse(Tokenizer().tok("")) == Null()

def test_parse_any_followed_by_literal():
    assert Parser()._parse(Tokenizer().tok("*abc")) == Any(Lit("abc"))

def test_parse_literal_followed_by_either():
    assert Parser()._parse(Tokenizer().tok("test*{pdf,txt}")) == Lit("test",Any(Either(Lit("pdf"), Lit("txt"))))

def test_parse_either_followed_by_lit():
    assert Parser()._parse(Tokenizer().tok("{macro,micro}soft")) == Either(Lit("macro"), Lit("micro"), Lit("soft"))