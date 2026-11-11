from split_theorem import split_theorem
from read_text_file import read_text_file

def label(labels):
    labels1 = {}
    for n, x in enumerate(labels):
        for label, pos in x:
            assert label not in labels1
            labels1[label] = (n, pos)
    return labels1

def read_theorem(theorem_name):
    s = read_text_file(theorem_name)
    variables, assumptions, result, proof, labels = split_theorem(s)
    labels = label(labels)
    return variables, assumptions, result, proof, labels
    
    
