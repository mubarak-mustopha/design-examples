import json
import sys

def do_add(env, args):
    assert len(args) == 2

    left = do(env, args[0])
    right = do(env, args[1])
    return left + right

def do_abs(env, args):
    assert len(args) == 1

    value = do(env, args[0])
    return abs(value)

def do_get(env, args):
    assert len(args) == 1 and isinstance(args[0], str)
    assert args[0] in env

    return env[args[0]]

def do_set(env, args):
    assert len(args) == 2 and isinstance(args[0], str)

    env[args[0]] = do(env, args[1])

def do_seq(env, args):
    assert len(args) > 0

    for expr in args:
        result = do(env, expr)
    
    return result

def do_comment(env, args):
    return None

def do_if(env, args):
    assert len(args) == 3
    cond = do(env, args[0])
    choice = args[1] if cond else args[2]
    return do(env, choice)

def do_array(env, args):
    assert len(args) == 1 and isinstance(args[0], int)
    return [None] * args[0] 

def do_set_array_elem(env, args):
    # stmt -> ['set-array-elm', var, idx, value]
    # args -> [var, idx, value]
    assert len(args) == 3
    array = do_get(env, [args[0]])

    idx, value = do(env, args[1]), do(env, args[2])
    assert isinstance(idx, int) and idx < len(array) 
    array[idx] = value

def do_get_array_elem(env, args):
    assert len(args) == 2
    array = do_get(env, [args[0]])

    idx = do(env, args[1])
    assert isinstance(idx, int) and idx < len(array) 
    return array[idx]

def do(env, expr):
    # an integer evaluates to itself 
    if isinstance(expr, int): return expr

    assert isinstance(expr, list)

    assert expr[0] in OPS, f"Unknown operation `{expr[0]}`"   

    func = OPS[expr[0]]
    return func(env, expr[1:])

OPS = {
    name.replace("do_", ""): func
    for name, func in globals().items()
    if name.startswith("do_")
}

def main():
    assert len(sys.argv) == 2, f"Usage: python expr.py file_name"
    with open(sys.argv[1], "r") as reader:
        program = json.load(reader)
    result = do({}, program)
    print(f"=> {result}")

if __name__=="__main__":
    main()