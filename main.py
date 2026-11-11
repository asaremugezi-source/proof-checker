from read_theorem import read_theorem
from prove_theorem import prove_theorem

def prove(theorem_name):
    return prove_theorem(read_theorem(theorem_name))

def main():
    print(prove("Theorem 2.theorem"))

if __name__ == "__main__":
    main()
