import math

def calculate_expression(alpha, beta):
    alpha_rad = math.radians(alpha)
    beta_rad = math.radians(beta)

    z = math.sin(alpha_rad + beta_rad) * math.sin(alpha_rad - beta_rad)
    return z

def days_to_exceed_distance(initial_distance, percent_increase):
    distance = initial_distance
    days = 1

    while distance <= 50:
        distance += distance * (percent_increase / 100)
        days += 1

    return days

def main():
    print("Задача 1: Обчислення z = sin(α + β) * sin(α - β)")
    alpha = float(input("Введіть значення α (у градусах): "))
    beta = float(input("Введіть значення β (у градусах): "))

    z = calculate_expression(alpha, beta)
    print(f"Результат обчислення z: {z:.4f}")

    print("\nЗадача 2: Підрахунок днів для перевищення 50 км")
    initial_distance = float(input("Введіть початкову відстань (М км): "))
    percent_increase = float(input("Введіть відсоток збільшення норми пробігу на день (K%): "))

    days = days_to_exceed_distance(initial_distance, percent_increase)
    print(f"Норма пробігу перевищить 50 км через {days} днів.")

if __name__ == "__main__":
    main()
