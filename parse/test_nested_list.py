from nested_list import tok_nested_list, parse_nested_list

def test_tok_empty_list():
    assert tok_nested_list("[]") == [["ListStart"], ["ListEnd"]]

def test_tok_flat_list():
    assert tok_nested_list("[1,2,3]") == [["ListStart"], ["Number", "1"], ["Number", "2"], ["Number", "3"],["ListEnd"]]

def test_tok_nested_list():
    assert tok_nested_list("[1, [2,3], 4]") == [["ListStart"], ["Number", "1"], ["ListStart"], ["Number", "2"], ["Number", "3"],["ListEnd"], ["Number", "4"], ["ListEnd"]]

def test_parse_empty_list():
    assert parse_nested_list(tok_nested_list("[]")) == list()

def test_parse_flat_list():
    assert parse_nested_list(tok_nested_list("[1,2,3]")) == [1,2,3]

def test_parse_nested_list():
    assert parse_nested_list(tok_nested_list("[1, [2,23], 4]")) == [1, [2,23], 4]
