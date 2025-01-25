def calculate_x(a, b):
    if a > b:
        return a * b + 21
    elif a == b:
        return -5
    elif a < b:
        return 3 * a / b + 1


def main():
    try:
        a = float(input("Введіть додатне число a: "))
        b = float(input("Введіть додатне число b: "))

        if a <= 0 or b <= 0:
            print("Помилка! Числа a та b повинні бути додатніми.")
            return

        x = calculate_x(a, b)
        print(f"Значення X: {x}")
    except ValueError:
        print("Помилка! Введені значення повинні бути числами.")


if __name__ == "__main__":
    main()
