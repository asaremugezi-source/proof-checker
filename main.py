from apply_axiom import apply_axiom
from read_axiom import read_axiom
s = read_axiom("Equivalance Relation - Reflexivity.axiom")
print(s)
print(apply_axiom(["a + b + c"], [], s))
