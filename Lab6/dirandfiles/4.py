def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")

count_lines("test.txt")