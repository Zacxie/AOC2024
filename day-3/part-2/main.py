import re
from utils import read_file_string, get_input_filename


def solve_puzzle(filename):
    s = read_file_string(filename)
    total = 0
    is_enabled = True

    matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", s)

    for match in matches:
        if match == "do()":
            is_enabled = True
        elif match == "don't()":
            is_enabled = False
        else:
            nums = [int(x) for x in re.findall(r'\d+', match)]
            if is_enabled:
                total += nums[0] * nums[1]

    return total


def main():
    filename = get_input_filename(use_sample=False)
    result = solve_puzzle(filename)
    print(f"Solution to part 2: {result}")


if __name__ == "__main__":
    main()