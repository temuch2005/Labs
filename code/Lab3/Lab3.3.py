def words_with_three_e(sentence):
    words = sentence.split()

    result = [word for word in words if word.count('е') == 3]

    return result


def main():
    sentence = input("Введіть речення: ")

    words = words_with_three_e(sentence)

    if words:
        print("Слова з трьома літерами 'е':")
        for word in words:
            print(word)
    else:
        print("У реченні немає слів з трьома літерами 'е'.")


if __name__ == "__main__":
    main()
