import json
import sys

def do_add(env, args):
    check(len(args) == 2, "Expected 2 arguments")

    left = do(env, args[0])
    right = do(env, args[1])
    return left + right

def do_abs(env, args):
    check(len(args) == 1, "Expected 1 argument")

    value = do(env, args[0])
    return abs(value)

def do_leq(env, args):
    check(len(args) == 2, "Expected 2 arguments for the `leq` statement")
    return do(env, args[0]) <= do(env, args[1])

def do_get(env, args):
    check(len(args) == 1 and isinstance(args[0], str), "Expected a string argument")
    check(args[0] in env, f"Unknown variable: {args[0]}")

    return env[args[0]]

def do_set(env, args):
    check(len(args) == 2 and isinstance(args[0], str), "Expected a string variable name and a value")

    env[args[0]] = do(env, args[1])

def do_seq(env, args):
    check(len(args) > 0, "Expected at least one expression")

    for expr in args:
        result = do(env, expr)
    
    return result

def do_comment(env, args):
    return None

def do_if(env, args):
    check(len(args) == 3, "Expected 3 arguments")
    cond = do(env, args[0])
    choice = args[1] if cond else args[2]
    return do(env, choice)

def do_array(env, args):
    check(len(args) == 1 and isinstance(args[0], int), "Expected an integer size")
    return [None] * args[0]

def do_set_array_elem(env, args):
    check(len(args) == 3, "Expected 3 arguments")
    array = do_get(env, [args[0]])

    idx, value = do(env, args[1]), do(env, args[2])
    check(isinstance(idx, int) and idx < len(array), "Array index out of bounds")
    array[idx] = value

def do_get_array_elem(env, args):
    check(len(args) == 2, "Expected 2 arguments")
    array = do_get(env, [args[0]])

    idx = do(env, args[1])
    check(isinstance(idx, int) and idx < len(array), "Array index out of bounds")
    return array[idx]

def do_catch(env, args):
    check(len(args) == 2, "Expected 2 arguments for `catch` statement")
    try:
        return do(env, args[0])
    except TLLException:
        return do(env, args[1])
    
def do_print(env, args):
    final = [arg if isinstance(arg, str) else str(do(env, arg)) for arg in args]
    print(' '.join(final)) 

def do_repeat(env, args):
    check(len(args) == 2, "Expected 2 argument for the `repeat` statement")
    check(isinstance(args[0], int), "1st argument must be an integer")

    count = args[0]
    while count > 0:
        do(env, args[1])
        count -= 1

def do(env, expr):
    # an integer evaluates to itself 
    if isinstance(expr, int): return expr

    check(isinstance(expr, list), "Expression must be a list")

    check(expr[0] in OPS, f"Unknown operation `{expr[0]}`")

    func = OPS[expr[0]]
    return func(env, expr[1:])

class TLLException(Exception):
    pass

def check(expr, error_msg: str):
    if not expr: raise TLLException(error_msg)

OPS = {
    name.replace("do_", ""): func
    for name, func in globals().items()
    if name.startswith("do_")
}

def main():
    check(len(sys.argv) == 2, "Usage: python expr.py file_name")
    with open(sys.argv[1], "r") as reader:
        program = json.load(reader)
    result = do({}, program)
    print(f"=> {result}")

if __name__=="__main__":
    main()