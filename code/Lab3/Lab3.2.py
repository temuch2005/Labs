def sum_ascii(word):
    total = 0
    for char in word:
        total += ord(char)
    return total

def main():
    word = input("Введіть слово: ")

    if word.strip() == "":
        print("Помилка! Ви ввели порожнє слово.")
    else:
        result = sum_ascii(word)
        print(f"Сума ASCII-кодів символів слова '{word}': {result}")

if __name__ == "__main__":
    main()
