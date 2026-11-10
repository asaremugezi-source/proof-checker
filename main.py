def read_text_file(file_name):
    x = open(file_name, "r")
    s = x.read()
    x.close()
    return s

def split_axiom(s):
    a = s.split("Assume:")
    assert(len(a) == 2)
    b = a.pop().split("Then:")
    assert(len(b) == 2)
    for bi in b:
        a.append(bi)
    return [ai.strip() for ai in a]



def read_axiom(axiom_name):
    return read_text_file(axiom_name)
    
    

s = read_axiom("Equivalance Relation - Reflexivity.axiom")
print(split_axiom(s))
