def create_text_file(file_name):
    try:
        with open(file_name, "w") as file:
            print("Введіть рядки тексту. Для завершення введіть порожній рядок.")
            while True:
                line = input("Рядок: ").strip()
                if line == "":
                    break
                file.write(line + "\n")
        print(f"Файл {file_name} успішно створено.")
    except Exception as e:
        print(f"Помилка при створенні файлу: {e}")


def process_text_file(input_file, output_file):
    try:
        with open(input_file, "r") as file_in, open(output_file, "w") as file_out:
            for line in file_in:
                line = line.strip()
                if len(line) < 20:
                    line = line.ljust(20)
                else:
                    line = line[:20]
                file_out.write(line + "\n")
        print(f"Файл {output_file} сформовано на основі {input_file}.")
    except FileNotFoundError:
        print(f"Помилка: файл {input_file} не знайдено.")
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")


def print_file_content(file_name):
    try:
        with open(file_name, "r") as file:
            print(f"\nВміст файлу {file_name}:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Помилка: файл {file_name} не знайдено.")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")


def main():
    input_file = "TF9_1.txt"
    output_file = "TF9_2.txt"

    while True:
        print("\nМеню:")
        print(">> 1 << Створити текстовий файл TF9_1")
        print(">> 2 << Формувати файл TF9_2 на основі TF9_1")
        print(">> 3 << Прочитати та вивести вміст файлу TF9_2")
        print(">> 0 << Вийти з програми")

        choice = input("Оберіть опцію: ").strip()

        if choice == "1":
            create_text_file(input_file)
        elif choice == "2":
            process_text_file(input_file, output_file)
        elif choice == "3":
            print_file_content(output_file)
        elif choice == "0":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
