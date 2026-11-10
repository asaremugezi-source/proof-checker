from split_axiom import split_axiom
def read_text_file(file_name):
    x = open(file_name, "r")
    s = x.read()
    x.close()
    return s

def find_substring(substring, string):
    ans = []
    for a in range(len(string)-len(substring)+1):
        if string[a:a+len(substring)] == substring:
            ans.append((a, a+len(substring)))
    return ans

def check_overlaps1(intervals):
    for i in range(len(intervals)-1):
        if intervals[i][1] > intervals[i+1][0]:
            return False
    return True

def check_overlaps(var_locations):
    for a in var_locations:
        for b in a:
            if not check_overlaps1([x[1:] for x in b]):
                return False
    return True

def find_variables(variables, assumptions, result):
    statements = [assumptions, result]
    ans = [[[] for i in statements[j]] for j in range(2)]
    for n, v in enumerate(variables):
        ans2 = []
        for i in range(2):
            for j in range(len(statements[i])):
                x = find_substring(v, statements[i][j])
                for a, b in x:
                    ans[i][j].append((n,a,b))
    ans = [[sorted(k, key = lambda x:x[1]) for k in j] for j in ans]
    assert(check_overlaps(ans)) 
    return ans



def read_axiom(axiom_name):
    variables, assumptions, result = split_axiom(read_text_file(axiom_name))
    var_locations = find_variables(variables, assumptions, result)
    return var_locations, assumptions, result

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
        
    
def apply_axiom(variables,
                known_results,
                var_locations,
                axiom_assumptions,
                axiom_result):
    requirements = write_statements(variables, var_locations[0], axiom_assumptions)
    if known_results == requirements:
        return write_statements(variables, var_locations[1], axiom_result)
    else:
        return False

s = read_axiom("Equivalance Relation - Transitivity.axiom")
print(apply_axiom(["x", "y", "z"], ["x = y", "y = z"], s[0], s[1], s[2]))
