import math

def shape_new(name):
    return {
        "name": name,
        "_class": Shape,
    }

def shape_density(sh, weight):
    return weight / call(sh, "area")   

Shape = {
    "classname": "Shape",
    "parent": None,
    "density": shape_density,
    "_new": shape_new
}

def square_area(sq):
    return sq["size"] ** 2

def square_perimeter(sq):
    return sq["size"] * 2

def square_new(name, size):
    return make(Shape, name) | {
        "size": size,
        "_class": Square
    }

Square = {
    "classname": "Square",
    "parent": Shape,
    "area": square_area,
    "perimeter": square_perimeter,
    "_new": square_new,
}


def circle_area(ci):
    return math.pi * ci["radius"] ** 2

def circle_perimeter(ci):
    return math.pi * ci["radius"] * 2

def circle_new(name, radius):
    return make(Shape, name) | {
        "radius": radius,
        "_class": Circle,
    }

Circle = {
    "classname": "Circle",
    "parent": Shape,
    "area": circle_area,
    "perimeter": circle_perimeter,
    "_new": circle_new,
}

def call(thing, method_name, *args):
    func = find(thing, method_name)
    return func(thing, *args)

def find(thing, method_name):
    func = find_in_cache(thing, method_name)
    if func is None:
        func = find_on_cls(thing["_class"], method_name)
        cache_method(thing, method_name, func)
    return func

def find_on_cls(cls, method_name):
    if cls is None:
        raise NotImplemented(method_name)
    else: 
        return cls.get(method_name) or find_on_cls(cls["parent"], method_name)

def find_in_cache(thing, method_name):
    return thing["_cache"].get(method_name)

def cache_method(thing, method_name, func):
    thing["_cache"][method_name] = func

def make(cls, *args):
    obj = cls["_new"](*args) | {"_cache": {}}
    return obj

things = [make(Square, "sq0", 3), make(Circle, "ci1", 2)]

for th in things:
    a = call(th, "area")
    p = call(th, "perimeter")
    d = call(th, "density", 5)
    print(f"I am {th['name']} with area {a:.2f}, density {d:.2f} and perimeter {p:.2f}")

