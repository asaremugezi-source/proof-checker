from apply_axiom import apply_axiom
from read_axiom import read_axiom
s = read_axiom("Equivalance Relation - Transitivity.axiom")
print(apply_axiom(["x", "y", "z"], ["x = y", "y = z"], s[0], s[1], s[2]))
