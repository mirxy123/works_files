import os

RESOURCE_DIR = os.path.join(os.path.dirname(__file__), "resource")


def count_lines_and_words(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Количество строк: {line_count}\n")
        f.write(f"Количество слов: {word_count}\n")

    print(f"Строк: {line_count}, слов: {word_count}")


if __name__ == "__main__":
    input_path = os.path.join(RESOURCE_DIR, "input.txt")
    output_path = os.path.join(RESOURCE_DIR, "statistics.txt")
    count_lines_and_words(input_path, output_path)