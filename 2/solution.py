def parse_1(filename):
    with open(filename, "r") as f:
        return [list(map(int, line.split())) for line in f]

def is_experiment_valid_1(nums):
    ascending = nums[0] < nums[1]
    for i1, i2 in zip(nums, nums[1:]):
        if ascending and i1 < i2 and i2 - i1 <= 3: 
            continue
        elif not ascending and i2 < i1 and i1 - i2 <= 3: 
            continue
        else:
            return False

    return True

def is_experiment_valid_2(nums):
    return any([is_experiment_valid_1(nums[0:i] + nums[i+1:]) for i in range(len(nums))])

def solve_1(input):    
    return sum([is_experiment_valid_1(exp) for exp in input])

def solve_2(input):
    return sum([is_experiment_valid_2(exp) for exp in input])


if __name__ == '__main__':
    print(solve_1(parse_1("input1.txt")))
    print(solve_2(parse_1("input1.txt")))
