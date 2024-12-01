def read_lists_from_file(filename):
    left_list = []
    right_list = []

    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                # Split line into two numbers
                left, right = line.strip().split()
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



# result = solve_puzzle('../sample-puzzle-input-part-1.txt')
result = solve_puzzle('../puzzle-input-part-1.txt')
print(f"Solution to part 1: {result}")