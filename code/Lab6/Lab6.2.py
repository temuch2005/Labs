def calculate_average_of_negatives(lst):
    negative_numbers = [num for num in lst if num < 0]

    if len(negative_numbers) == 0:
        print("У списку немає від'ємних елементів.")
        return None

    average = sum(negative_numbers) / len(negative_numbers)
    return average

def main():
    try:
        user_input = input("Введіть список чисел, розділених пробілом: ")
        user_list = list(map(int, user_input.split()))
    except ValueError:
        print("Помилка: введіть тільки цілі числа.")
        return

    average = calculate_average_of_negatives(user_list)

    if average is not None:
        print(f"Середнє арифметичне від'ємних чисел: {average:.2f}")

if __name__ == "__main__":
    main()
