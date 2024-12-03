import re

MUL_INSTRUCTION_FORMAT = r"(mul)\(([0-9]{1,3}),([0-9]{1,3})\)"
DO_DONT_MUL_INSTRUCTION_FORMAT = r"(do|don\'t|mul)\((?:([0-9]{1,3}),([0-9]{1,3}))?\)"

def parse_1(filename):
    with open(filename, "r") as f:
        matches = re.findall(MUL_INSTRUCTION_FORMAT, f.read())
        return [(instr, int(n1), int(n2)) for instr, n1, n2 in matches]

def parse_2(filename):
    with open(filename, "r") as f:
        matches = re.findall(DO_DONT_MUL_INSTRUCTION_FORMAT, f.read())
        return [(instr, int(n1), int(n2)) if instr == "mul" else (instr, "", "") for instr, n1, n2 in matches]

def solve_1(input):    
    return sum([n1 * n2 for instr, n1, n2 in input])

def solve_2(input):
    result = 0
    should_mul = True
    for i, n1, n2 in input:
        if i == "do":
            should_mul = True
        elif i == "don't":
            should_mul = False
        elif i == "mul":
            result += n1*n2 if should_mul else 0
        else:
            "ERROR: Unsupported instruction"
            return

    return result

if __name__ == '__main__':
    print(solve_1(parse_1("input1.txt")))
    print(solve_2(parse_2("input1.txt")))
