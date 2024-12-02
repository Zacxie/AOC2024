from utils import read_file_lines, get_input_filename

def read_lists_from_file(filename):
    left_list = []
    right_list = []

    for line in read_file_lines(filename):
        # Split line into two numbers
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

    return left_list, right_list


def calculate_total_distance(left_list, right_list):
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)

    # Calculate distances between pairs
    total_distance = 0
    for num1, num2 in zip(sorted_left, sorted_right):
        distance = abs(num1 - num2)
        total_distance += distance

    return total_distance


def solve_puzzle(filename):
    left_list, right_list = read_lists_from_file(filename)

    return calculate_total_distance(left_list, right_list)


def main():
    filename = get_input_filename(use_sample=False)
    result = solve_puzzle(filename)
    print(f"Solution to part 1: {result}")


if __name__ == "__main__":
    main()