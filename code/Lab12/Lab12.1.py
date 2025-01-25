import json

def read_json_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Помилка: файл {file_name} не знайдено.")
        return []
    except json.JSONDecodeError:
        print(f"Помилка: файл {file_name} має некоректний формат JSON.")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу {file_name}: {e}")
        return []


def write_json_file(file_name, data):
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Дані успішно записано у файл {file_name}.")
    except Exception as e:
        print(f"Помилка при записі у файл {file_name}: {e}")


def print_json_content(file_name):
    data = read_json_file(file_name)
    if data:
        print(json.dumps(data, ensure_ascii=False, indent=4))
    else:
        print("Файл порожній або не існує.")


def add_record(file_name):
    data = read_json_file(file_name)
    new_record = {
        "прізвище": input("Введіть прізвище: ").strip(),
        "ім'я": input("Введіть ім'я: ").strip(),
        "адреса": input("Введіть адресу: ").strip(),
        "номер школи": input("Введіть номер школи: ").strip(),
        "клас": int(input("Введіть номер класу (цифра): ").strip()),
        "день відвідування": input("Введіть день відвідування гуртка (субота чи неділя): ").strip().lower()
    }
    data.append(new_record)
    write_json_file(file_name, data)


def delete_record(file_name):
    data = read_json_file(file_name)
    surname = input("Введіть прізвище запису для видалення: ").strip()
    updated_data = [record for record in data if record.get("прізвище") != surname]
    if len(data) == len(updated_data):
        print("Запис із таким прізвищем не знайдено.")
    else:
        write_json_file(file_name, updated_data)


def search_records(file_name):
    data = read_json_file(file_name)
    if not data:
        return
    field = input("Введіть поле для пошуку (прізвище, ім'я, адреса, номер школи, клас, день відвідування): ").strip()
    value = input("Введіть значення для пошуку: ").strip()
    results = [record for record in data if str(record.get(field, "")).lower() == value.lower()]
    if results:
        print("Результати пошуку:")
        print(json.dumps(results, ensure_ascii=False, indent=4))
    else:
        print("Записів не знайдено.")


def process_task(file_name, output_file):
    data = read_json_file(file_name)
    results = [
        {
            "прізвище": record["прізвище"],
            "ім'я": record["ім'я"],
            "адреса": record["адреса"]
        }
        for record in data
        if record.get("клас") in [7, 8] and record.get("день відвідування") == "субота"
    ]
    write_json_file(output_file, results)
    print("Результати завдання записані у файл", output_file)


def main():
    input_file = "students.json"
    output_file = "results.json"

    while True:
        print("\nМеню:")
        print(">> 1 << Вивести вміст JSON-файлу")
        print(">> 2 << Додати новий запис у JSON-файл")
        print(">> 3 << Видалити запис із JSON-файлу")
        print(">> 4 << Знайти записи у JSON-файлі")
        print(">> 5 << Виконати завдання та зберегти результат")
        print(">> 0 << Вийти з програми")

        choice = input("Оберіть опцію: ").strip()

        if choice == "1":
            print_json_content(input_file)
        elif choice == "2":
            add_record(input_file)
        elif choice == "3":
            delete_record(input_file)
        elif choice == "4":
            search_records(input_file)
        elif choice == "5":
            process_task(input_file, output_file)
        elif choice == "0":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
