import os

RESOURCE_DIR = os.path.join(os.path.dirname(__file__), "resource")


def sort_words(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        words = [line.strip() for line in f if line.strip()]

    sorted_alphabetically = sorted(words)
    sorted_by_length = sorted(words, key=len)
    sorted_reverse = sorted(words, reverse=True)

    outputs = {
        "sorted_alphabetically.txt": sorted_alphabetically,
        "sorted_by_length.txt": sorted_by_length,
        "sorted_reverse.txt": sorted_reverse,
    }

    for filename, word_list in outputs.items():
        path = os.path.join(RESOURCE_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(word_list) + "\n")
        print(f"Записано: {path}")


if __name__ == "__main__":
    words_path = os.path.join(RESOURCE_DIR, "words.txt")
    sort_words(words_path)