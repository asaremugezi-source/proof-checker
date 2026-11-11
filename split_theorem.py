import split_axiom
from find_in_brackets import find_in_brackets

def split_theorem1(s):
    return [x.strip() for x in s.split("Proof:")]


def split_proof1(s):
    return [a.strip() for a in s.split("&")]

def split_statement1(s): #statement -> claim, axiom_name, variables, references
    a, b = find_in_brackets(s, "[", "]")
    claim = s[:a-1] + s[b+1:]
    ans = []
    axiom = s[a:b]
    var1, var2 = find_in_brackets(axiom, "(", ")")
    ref1, ref2 = find_in_brackets(axiom, "{", "}")
    axiom_name = axiom[:min(var1, ref1)-1]
    variables = axiom[var1:var2]
    references = axiom[ref1:ref2]
    return claim, axiom_name, variables, references

def split_statement(s):
    claim, axiom_name, variables, references = split_statement1(s)
    claim = claim.strip()
    axiom_name = axiom_name.strip()
    variables = [x.strip() for x in variables.split(",")]
    references1 = [x.strip() for x in references.split(".")]
    references = []
    for x in references1:
        if x != "":
            references.append(x)
    return claim, axiom_name, variables, references

def split_statements(s):
    ans = []
    for statement in s:
        ans.append(split_statement(statement))
    return ans
    
def remove_label(a):
    for i in range(len(a)):
        if a[i] == ".":
            return [a[:i].strip(), a[i+1:].strip()]
    return [a]
    
def remove_labels(statements):
    x = [remove_label(a) for a in statements]
    labels = []
    statements = []
    for n, a in enumerate(x):
        if len(a) == 2:
            labels.append((a[0], n))
        statements.append(a[-1])
    return labels, statements

def split_theorem(s):
    axiom, proof = split_theorem1(s)
    proof = split_axiom.split_statements(proof)
    variables, assumptions, result = split_axiom.split_axiom(axiom)
    labels = [[],[]]
    labels[0], assumptions = remove_labels(assumptions)
    labels[1], proof = remove_labels(proof)
    proof = split_statements(proof)
    return variables, assumptions, result, proof, labels

if __name__ == "__main__":
    from read_text_file import read_text_file
    s = read_text_file("Theorem 1.theorem")
    for a in split_theorem(s):
        print(a)
