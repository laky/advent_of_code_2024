"""
-- Prompt 1:
Solve the below algorithmic problem using Python. Include the code to process the input from a text file.

"Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians head out to take a look.

The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"

The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?


-- Code in the answer:
import re

def process_memory(file_path):
    # Read the input file
    with open(file_path, 'r') as file:
        memory = file.read()
    
    # Regular expression to match valid mul instructions: mul(X,Y) where X and Y are numbers
    pattern = r'mul\((\d+),(\d+)\)'
    
    # Find all matches
    matches = re.findall(pattern, memory)
    
    # Compute the sum of the results of the valid instructions
    total = sum(int(x) * int(y) for x, y in matches)
    
    return total

# Example usage
input_file = "input1.txt"  # Replace with the actual path to your input file
result = process_memory(input_file)
print(f"Total sum of valid 'mul' instructions: {result}")


-- Prompt 2:
That's correct! Now add to the original file a function to print a solution to a second problem below. Your python code should output both answers.

As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?
"""

import re

def process_memory(file_path):
    # Read the input file
    with open(file_path, 'r') as file:
        memory = file.read()
    
    # Regular expression to match valid mul instructions: mul(X,Y) where X and Y are numbers
    mul_pattern = r'mul\((\d+),(\d+)\)'
    
    # Regular expression to match do() and don't() instructions
    control_pattern = r'do\(\)|don\'t\(\)'
    
    # Find all mul matches
    mul_matches = re.findall(mul_pattern, memory)
    
    # Find all control statements and their positions
    controls = [(m.start(), m.group()) for m in re.finditer(control_pattern, memory)]
    
    # Solution for problem 1: Sum of all valid mul instructions
    total_sum_all = sum(int(x) * int(y) for x, y in mul_matches)
    
    # Solution for problem 2: Sum of enabled mul instructions based on control statements
    enabled = True  # Default state: enabled
    total_sum_enabled = 0
    
    current_control_index = 0  # Index to track which control statement applies
    mul_positions = [m.start() for m in re.finditer(mul_pattern, memory)]
    
    for i, mul_pos in enumerate(mul_positions):
        # Check if we need to update the control state
        while current_control_index < len(controls) and controls[current_control_index][0] < mul_pos:
            if controls[current_control_index][1] == "do()":
                enabled = True
            elif controls[current_control_index][1] == "don't()":
                enabled = False
            current_control_index += 1
        
        # Add to the total sum only if mul is enabled
        if enabled:
            x, y = map(int, mul_matches[i])
            total_sum_enabled += x * y
    
    return total_sum_all, total_sum_enabled

# Example usage
input_file = "input1.txt"  # Replace with the actual path to your input file
total_all, total_enabled = process_memory(input_file)

print(f"Total sum of all valid 'mul' instructions (Problem 1): {total_all}")
print(f"Total sum of enabled 'mul' instructions (Problem 2): {total_enabled}")
