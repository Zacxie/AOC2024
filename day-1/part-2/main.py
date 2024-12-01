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


def calculate_similarity_score(left_list, right_list):
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1

    total_score = 0
    for num in left_list:
        # Multiply number by its count in right list (0 if not present)
        count = right_counts.get(num, 0)
        total_score += num * count

    return total_score



# left_list, right_list = read_lists_from_file('../sample-puzzle-input-part-1.txt')
left_list, right_list = read_lists_from_file('../puzzle-input-part-1.txt')
result = calculate_similarity_score(left_list, right_list)
print(f"Solution to part 2: {result}")