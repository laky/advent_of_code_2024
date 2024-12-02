from collections import defaultdict

def parse_1(filename):
    with open(filename, "r") as f:
        nums = f.read().split()
        first_list = list(map(int, nums[::2]))
        second_list = list(map(int, nums[1::2]))
        return first_list, second_list

def solve_1(input):    
    return sum(map(lambda a, b: abs(a-b), sorted(input[0]), sorted(input[1])))

def solve_2(input):
    x_to_counts = defaultdict(int)
    for y in input[1]:
        x_to_counts[y] += 1
    return sum([x * x_to_counts[x] for x in input[0]])


if __name__ == '__main__':
    print(solve_1(parse_1("input1.txt")))
    print(solve_2(parse_1("input1.txt")))
