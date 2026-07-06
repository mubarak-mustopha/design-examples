import string

DIGITS = string.digits

def tok_nested_list(expr):
    toks = []
    num_seq = ""
    for char in expr:
        if char == "[":
            toks.append(["ListStart"])
        elif char in DIGITS:
            num_seq += char
        elif char == ",":
            if num_seq: 
                toks.append(["Number", num_seq])
                num_seq = ""
        elif char == "]":
            if num_seq: 
                toks.append(["Number", num_seq])
                num_seq = ""
            toks.append(["ListEnd"])
        elif char == " ":
            continue
        else:
            raise NotImplementedError(f"Unknown token {char}")
        
    return toks
            

def parse_nested_list(tokens):
    if len(tokens) == 0 or tokens[0][0] != "ListStart":
        raise NotImplementedError("Invalid list expression")
    
    stack = [list()] 
    top = stack[-1]
    index = 1

    while index < len(tokens) and len(stack) > 0:
        current = tokens[index]
        if current[0] == 'Number':
            top.append(int(current[1]))
        elif current[0] == 'ListStart':
            next = list()
            top.append(next)
            stack.append(next)
            top = next
        else: # ListEnd
            stack.pop()
            if not stack:
                break
            top = stack[-1]

        index += 1

    if index == len(tokens) - 1:
        return top
    else:
        raise NotImplementedError("Invalid list expression")
    
