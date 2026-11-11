def write_statement(variables, var_locations, statement):
    s = []
    i1 = 0
    i2 = 0
    while i1 < len(statement):
        if i2 < len(var_locations) and i1 >= var_locations[i2][1]:
            s.append(variables[var_locations[i2][0]])
            i1 = var_locations[i2][2]
            i2 += 1
        else:
            s.append(statement[i1]) 
            i1 += 1
    return "".join(s)

def write_statements(variables, var_locations, statements):
    ans = []
    for a in range(len(statements)):
        ans.append(write_statement(variables, var_locations[a], statements[a]))
    return ans
        
    
def apply_axiom(variables, known_results, axiom):
    var_locations, axiom_assumptions, axiom_result = axiom
    requirements = write_statements(variables, var_locations[0], axiom_assumptions)
    if known_results == requirements:
        return set(write_statements(variables, var_locations[1], axiom_result))
    else:
        return set()
