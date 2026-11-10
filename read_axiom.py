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
