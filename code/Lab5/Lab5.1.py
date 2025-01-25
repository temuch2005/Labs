def main():
    while True:
        try:
            n = int(input("Введіть довжину масиву (N): "))
            if n > 0:
                break
            else:
                print("Довжина масиву має бути додатнім числом!")
        except ValueError:
            print("Будь ласка, введіть ціле число!")

    array = []
    print(f"Введіть {n} цілих чисел для масиву:")
    for i in range(n):
        while True:
            try:
                num = int(input(f"Елемент {i + 1}: "))
                array.append(num)
                break
            except ValueError:
                print("Будь ласка, введіть ціле число!")

    total_sum = sum(x for x in array if x > 0 and x % 3 == 0)

    print(f"Сума додатніх елементів, кратних трьом: {total_sum}")

if __name__ == "__main__":
    main()