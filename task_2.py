import os

RESOURCE_DIR = os.path.join(os.path.dirname(__file__), "resource")


def search_word(text_file, output_file):
    search = input("Введите слово для поиска: ")

    with open(text_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    count = 0
    line_numbers = []

    for i, line in enumerate(lines, start=1):
        occurrences = line.lower().count(search.lower())
        if occurrences > 0:
            count += occurrences
            line_numbers.append(i)

    found = count > 0

    print(f"Слово найдено: {'да' if found else 'нет'}")
    print(f"Количество вхождений: {count}")
    print(f"Номера строк: {line_numbers}")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Слово: {search}\n")
        f.write(f"Найдено: {'да' if found else 'нет'}\n")
        f.write(f"Количество вхождений: {count}\n")
        f.write(f"Номера строк: {line_numbers}\n")


if __name__ == "__main__":
    text_path = os.path.join(RESOURCE_DIR, "text.txt")
    output_path = os.path.join(RESOURCE_DIR, "search_results.txt")
    search_word(text_path, output_path)