import os

RESOURCE_DIR = os.path.join(os.path.dirname(__file__), "resource")


def combine_files(files, output_file):
    with open(output_file, "w", encoding="utf-8") as out:
        for i, file_name in enumerate(files):
            out.write(f"=== Содержимое {os.path.basename(file_name)} ===\n")
            with open(file_name, "r", encoding="utf-8") as f:
                content = f.read().strip()
            out.write(content + "\n")
            if i < len(files) - 1:
                out.write("\n")

    print(f"Файлы объединены в {output_file}")


if __name__ == "__main__":
    input_files = [
        os.path.join(RESOURCE_DIR, "file1.txt"),
        os.path.join(RESOURCE_DIR, "file2.txt"),
        os.path.join(RESOURCE_DIR, "file3.txt"),
    ]
    output_path = os.path.join(RESOURCE_DIR, "combined.txt")
    combine_files(input_files, output_path)