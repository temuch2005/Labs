def delete_element_from_list(lst, element):
    if element in lst:
        lst.remove(element)
        print(f"Елемент '{element}' видалено зі списку.")
    else:
        print(f"Елемент '{element}' не знайдено у списку.")
    return lst

def main():
    user_input = input("Введіть список чисел або слів, розділених пробілом: ")
    user_list = user_input.split()

    element_to_remove = input("Введіть елемент, який потрібно видалити: ")

    updated_list = delete_element_from_list(user_list, element_to_remove)

    print("Оновлений список:", updated_list)

if __name__ == "__main__":
    main()
