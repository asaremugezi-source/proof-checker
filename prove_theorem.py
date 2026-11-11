from read_axiom import read_axiom
from apply_axiom import apply_axiom
from read_theorem import read_theorem
from read_axiom import find_variables
def prove_statement(claim, axiom_name, variables, known_results):
    if axiom_name.split(".")[1] == "axiom":
        axiom = read_axiom(axiom_name)
        return claim in apply_axiom(variables, known_results, axiom)
    else:
        theorem = read_theorem(axiom_name)
        return claim in apply_theorem(variables, known_results, theorem)

def apply_theorem(variables, known_results, theorem):
    if not prove_theorem(theorem):
        return set()
    variables1, assumptions, result, _, _ = theorem
    
    var_locations = find_variables(variables1, assumptions, result)
    axiom = var_locations, assumptions, result
    return apply_axiom(variables, known_results, axiom)

def find_references(references, labels, assumptions, proof, n):
    known_results = []
    for reference in references:
        a, b = labels[reference]
        assert a == 0 or b < n
        if a == 0:
            known_results.append(assumptions[b])
        else:
            known_results.append(proof[b][0])
    return known_results
            


def prove_theorem(theorem):
    _,assumptions, result, proof, labels = theorem
    proven = set()
    for n, statement in enumerate(proof):
        
        claim, axiom_name, variables, references = statement
        known_results = find_references(references, labels, assumptions, proof, n)
        if not prove_statement(claim, axiom_name, variables, known_results):
            return False
        proven.add(claim)
    for x in result:
        if x not in proven:
            return False
    return True

if __name__ == "__main__":
    s = read_theorem("Theorem 1.theorem")
    print(prove_theorem(s))
