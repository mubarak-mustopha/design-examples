from arithmetic import parse_arithmetic

def test_parse_expr_with_single_addition():
    assert parse_arithmetic('1 + 2') == ['+', '1', '2']

def test_parse_expr_with_single_multiplication():
    assert parse_arithmetic('1 * 2') == ['*', '1', '2']

def test_parse_expr_lower_operator_seen_first():
    assert parse_arithmetic('1 + 2 * 3') == ['+', '1', ['*', '2', '3']]

def test_parse_expr_higher_operator_seen_first():
    assert parse_arithmetic('1 * 2 + 3') == ['+', ['*', '1', '2'], '3']

def test_parse_expr_same_operator_seen_twice():
    assert parse_arithmetic('1 + 2 + 3') == ['+', ['+', '1', '2'], '3']

def test_parse_diff_operators_same_precedence():
    assert parse_arithmetic('1 * 2 / 3') == ['/', ['*', '1', '2'], '3']

def test_parse_expr_same_operator_four_times():
    assert parse_arithmetic('1 + 2 + 3 + 4') == ['+', ['+', ['+', '1', '2'], '3'], '4']

def test_parse_expr_high_low_high_operators():
    assert parse_arithmetic('1 * 2 + 3 * 4') == ['+', ['*', '1', '2'], ['*', '3', '4']]

def test_parse_expr_low_hight_low_operators():
    assert parse_arithmetic('1 + 2 * 3 + 4') == [ '+', ['+', '1', ['*', '2', '3']], '4']

def test_parse_extra_long_expr():
    assert parse_arithmetic('1 + 2 + 3 * 5 + 4 * 3') == ['+', ['+',['+','1','2'], ['*', '3', '5']],['*','4','3']]