def split_axiom1(s):
    a = s.split("Assume:")
    assert(len(a) == 2)
    b = a.pop().split("Then:")
    assert(len(b) == 2)
    for bi in b:
        a.append(bi)
    return [ai.strip() for ai in a]

def split_axiom2(axiom):
    return [split_variables(axiom[0]), split_statements(axiom[1]), split_statements(axiom[2])]

def split_axiom(axiom):
    return split_axiom2(split_axiom1(axiom))

def split_statements(statements):
    return [x.strip() for x in statements.split("&")]

def split_variables(variables):
    return [x.strip() for x in variables.split(" ")]
