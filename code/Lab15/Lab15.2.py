import pandas as pd
import matplotlib.pyplot as plt

def read_csv(file_path):
    try:
        data = pd.read_csv(file_path, encoding='utf-8')
        data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
        return data
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено. Перевірте шлях до файлу.")
        return None
    except Exception as e:
        print(f"Виникла помилка при читанні файлу: {e}")
        return None

def main():
    input_file = "comptage_velo.csv"

    data = read_csv(input_file)
    if data is None:
        return

    year = 2011
    data['Year'] = data['Date'].dt.year
    yearly_data = data[data['Year'] == year]

    if yearly_data.empty:
        print(f"Дані за {year} рік відсутні у файлі.")
        return

    monthly_data = yearly_data.groupby(yearly_data['Date'].dt.month).sum(numeric_only=True)

    months = [
        "Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень",
        "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"
    ]

    most_popular_month = monthly_data['Total'].idxmax()
    print(f"Найбільш популярний місяць: {months[most_popular_month - 1]}")

    plt.figure(figsize=(10, 6))
    plt.plot(monthly_data.index, monthly_data['Total'], marker='o', label='Використання велодоріжок')
    plt.title(f'Використання велодоріжок за {year} рік', fontsize=14)
    plt.xlabel('Місяці', fontsize=12)
    plt.ylabel('Кількість велосипедистів', fontsize=12)
    plt.grid()
    plt.legend()
    plt.xticks(range(1, 13), months, rotation=45)
    plt.show()

if __name__ == "__main__":
    main()

