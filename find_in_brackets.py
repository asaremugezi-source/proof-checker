def find_in_brackets(statement, open_bracket, close_bracket):
    count = 0
    size = 0
    for n, c in enumerate(statement):
        if count > 0:
            size +=  1
        if c == open_bracket:
            count += 1
        elif c == close_bracket:
            count -= 1
        if count == 0 and size > 0:
            return(n-size+1, n)
    return -1, -1

            
