def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

def main():
    start = 5
    end = 25

    fibonacci_sequence = [fibonacci(i) for i in range(start, end + 1)]

    print("Числа Фібоначчі з 5-го по 25-й член:")
    print(fibonacci_sequence)

    count = len(fibonacci_sequence)
    print(f"Кількість чисел у ряді: {count}")


if __name__ == "__main__":
    main()
