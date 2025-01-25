def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

def main():
    try:
        n = int(input("Введіть ціле число N (1 < N < 9): "))

        if n <= 1 or n >= 9:
            print("Помилка! Число N повинно бути в межах 1 < N < 9.")
            return

        print_pattern(n)
    except ValueError:
        print("Помилка! Введене значення повинно бути цілим числом.")


if __name__ == "__main__":
    main()
