operators = ['+', '-', '*', '/']

def parse_arithmetic(arithmetic_str):
    operand_to_consume = None

    expr_lst = []
    tokens = arithmetic_str.split()

    i = 0
    while (i < len(tokens)):
        tok = tokens[i]
        if tok.isdigit():
            operand_to_consume = tok
        
        elif tok in operators:
            if expr_lst == []:
                expr_lst = [tok, operand_to_consume]

                if tok in ['*', '/']:
                    expr_lst.append(tokens[i + 1])
                    i += 1
            
            elif tok in ['*', '/']:
                if operand_to_consume: 
                    # preceded by a + or - e.g a + b * c -> [+, a, [*, b, c]]
                    sub_expr = [tok, operand_to_consume, tokens[i + 1]]
                    expr_lst.append(sub_expr)

                else: 
                    # preceded by * or / e.g a / b * c -> [*, [/, a, b], c]
                    expr_lst = [tok, expr_lst, tokens[i + 1]]

                i += 1

            else:
                if operand_to_consume:
                    expr_lst.append(operand_to_consume)
                expr_lst = [tok, expr_lst]

            operand_to_consume = None

        else:
            raise NotImplemented(f"Unknown token `{tok}`")
        
        i += 1
                    
    if len(expr_lst) < 3:
        expr_lst.append(operand_to_consume)

    return expr_lst


