def display_all_students(data):
    print("\nВсі учні в словнику:")
    for key, value in data.items():
        print(f"{key}: {value}")

def add_student(data):
    try:
        surname = input("Введіть прізвище: ").strip()
        name = input("Введіть ім'я: ").strip()
        address = input("Введіть адресу: ").strip()
        school_number = int(input("Введіть номер школи: ").strip())
        school_class = int(input("Введіть клас: ").strip())

        student_id = len(data) + 1
        data[student_id] = {
            "Прізвище": surname,
            "Ім'я": name,
            "Адреса": address,
            "Номер школи": school_number,
            "Клас": school_class
        }
        print("Новий запис додано успішно!")
    except ValueError:
        print("Помилка: Некоректні дані!")

def remove_student(data):
    try:
        student_id = int(input("Введіть ID учня для видалення: ").strip())
        if student_id in data:
            del data[student_id]
            print("Запис успішно видалено!")
        else:
            print("Помилка: Учня з таким ID не існує.")
    except ValueError:
        print("Помилка: Введіть коректне число!")

def display_sorted_students(data):
    print("\nУчні за відсортованими ключами:")
    for key in sorted(data.keys()):
        print(f"{key}: {data[key]}")

def find_senior_students(data):
    try:
        school_number = int(input("Введіть номер школи для пошуку: ").strip())
        senior_students = {
            key: (value["Прізвище"], value["Ім'я"], value["Адреса"])
            for key, value in data.items()
            if value["Номер школи"] == school_number and value["Клас"] in (10, 11)
        }
        if senior_students:
            print("\nУчні 10-11 класів у школі", school_number)
            for key, value in senior_students.items():
                print(f"ID {key}: {value}")
        else:
            print("У заданій школі немає учнів 10-11 класів.")
    except ValueError:
        print("Помилка: Введіть коректне число!")


def main():
    students = {
        1: {"Прізвище": "Іваненко", "Ім'я": "Іван", "Адреса": "вул. Шевченка, 10", "Номер школи": 5, "Клас": 11},
        2: {"Прізвище": "Петренко", "Ім'я": "Петро", "Адреса": "вул. Грушевського, 20", "Номер школи": 3, "Клас": 9},
        3: {"Прізвище": "Сидоренко", "Ім'я": "Олена", "Адреса": "вул. Франка, 30", "Номер школи": 5, "Клас": 10},
        4: {"Прізвище": "Коваленко", "Ім'я": "Анна", "Адреса": "вул. Січових Стрільців, 40", "Номер школи": 1,
            "Клас": 8},
        5: {"Прізвище": "Шевченко", "Ім'я": "Михайло", "Адреса": "вул. Лесі Українки, 50", "Номер школи": 3,
            "Клас": 11},
        6: {"Прізвище": "Гнатенко", "Ім'я": "Олег", "Адреса": "вул. Чорновола, 60", "Номер школи": 2, "Клас": 7},
    }

    while True:
        print("\nМеню:")
        print(">>1<< Вивести всі записи словника")
        print(">>2<< Додати нового учня")
        print(">>3<< Видалити учня")
        print(">>4<< Вивести словник за відсортованими ключами")
        print(">>5<< Знайти учнів старших класів у заданій школі")
        print(">>0<< Вийти з програми")
        choice = input("Оберіть опцію: ").strip()

        if choice == "1":
            display_all_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            remove_student(students)
        elif choice == "4":
            display_sorted_students(students)
        elif choice == "5":
            find_senior_students(students)
        elif choice == "0":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
