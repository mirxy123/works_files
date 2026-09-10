import os

RESOURCE_DIR = os.path.join(os.path.dirname(__file__), "resource")
SHIFT = 3
ALPHABET_SIZE = 26


def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % ALPHABET_SIZE + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)


def encrypt_file(input_file, output_file, shift=SHIFT):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    encrypted = caesar_cipher(text, shift)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(encrypted)

    print(f"Зашифровано в {output_file}")


def decrypt_file(input_file, output_file, shift=SHIFT):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    decrypted = caesar_cipher(text, -shift)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(decrypted)

    print(f"Расшифровано в {output_file}")


if __name__ == "__main__":
    secret_path = os.path.join(RESOURCE_DIR, "secret.txt")
    encrypted_path = os.path.join(RESOURCE_DIR, "encrypted.txt")
    decrypted_path = os.path.join(RESOURCE_DIR, "decrypted.txt")

    encrypt_file(secret_path, encrypted_path)
    decrypt_file(encrypted_path, decrypted_path)