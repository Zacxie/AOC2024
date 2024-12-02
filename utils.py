def read_file_lines(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]


def get_input_filename(use_sample=False):
    return "../sample-puzzle-input.txt" if use_sample else "../puzzle-input.txt"