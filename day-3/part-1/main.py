from utils import read_file_lines, get_input_filename


def is_digits_only(text):
    return all(c.isdigit() for c in text)


def find_valid_multiplications(text):
    total = 0
    i = 0

    while i < len(text) - 3:
        if text[i:i + 4] == 'mul(':
            i += 4

            num1 = ""
            while i < len(text) and text[i].isdigit():
                num1 += text[i]
                i += 1

            if not (1 <= len(num1) <= 3) or i >= len(text) or text[i] != ',':
                i += 1
                continue

            i += 1

            num2 = ""
            while i < len(text) and text[i].isdigit():
                num2 += text[i]
                i += 1

            if not (1 <= len(num2) <= 3) or i >= len(text) or text[i] != ')':
                i += 1
                continue

            if is_digits_only(num1) and is_digits_only(num2):
                total += int(num1) * int(num2)

        i += 1

    return total


def solve_puzzle(filename):
    total = 0

    for line in read_file_lines(filename):
        total += find_valid_multiplications(line)

    return total


def main():
    filename = get_input_filename(use_sample=False)
    result = solve_puzzle(filename)
    print(f"Solution to part 1: {result}")


if __name__ == "__main__":
    main()