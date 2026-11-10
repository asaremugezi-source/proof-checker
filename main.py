from split_axiom import split_axiom
def read_text_file(file_name):
    x = open(file_name, "r")
    s = x.read()
    x.close()
    return s

def find_substring(substring, string):
    ans = []
    for a in range(len(string)-len(substring)):
        if string[a:a+len(substring)] == substring:
            ans.append((a, a+len(substring)))
    return ans


def find_variables(variables, assumptions, result):
    a = [x. strip() for x in variables.split(" ")]
    b = []
    c = []
    for v in a:
        b.append(find_substring(v, assumptions))
        c.append(find_substring(v, result))
    return b, c

def read_axiom(axiom_name):
    x = read_text_file(axiom_name)
    print(split_axiom(x))
    
s = read_axiom("Equivalance Relation - Transitivity.axiom")
