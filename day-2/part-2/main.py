from utils import read_file_lines, get_input_filename


def is_safe_report(levels):
    if len(levels) < 2:
        return False

    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    first_diff = differences[0]
    should_increase = first_diff > 0

    for diff in differences:
        if should_increase and diff <= 0:
            return False
        if not should_increase and diff >= 0:
            return False
        if abs(diff) < 1 or abs(diff) > 3:
            return False

    return True


def is_safe_with_dampener(levels):
    # check if safe without removing any levels
    if is_safe_report(levels):
        return True

    # bruteforce that bitch
    for i in range(len(levels)):
        dampened_levels = levels[:i] + levels[i + 1:]

        if is_safe_report(dampened_levels):
            return True

    return False


def count_safe_reports(filename):
    safe_count = 0

    for line in read_file_lines(filename):
        levels = [int(x) for x in line.split()]

        if is_safe_with_dampener(levels):
            safe_count += 1

    return safe_count


def main():
    filename = get_input_filename(use_sample=False)
    result = count_safe_reports(filename)

    if result is not None:
        print(f"Solution to part 2: {result}")


if __name__ == "__main__":
    main()