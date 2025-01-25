import csv

def read_csv(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено. Перевірте шлях до файлу.")
        return None
    except Exception as e:
        print(f"Виникла помилка при читанні файлу: {e}")
        return None

def write_csv(file_path, data, fieldnames):
    try:
        with open(file_path, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
            print(f"Результати збережено у файл: {file_path}")
    except Exception as e:
        print(f"Виникла помилка при записі файлу: {e}")

def main():
    input_file = "exports_data.csv"
    output_file = "filtered_countries.csv"

    data = read_csv(input_file)
    if not data:
        return

    print("Вміст CSV файлу:")
    for row in data[:10]:
        print(row)

    search_countries = input("Введіть назви країн через кому: ").split(",")
    search_countries = [country.strip() for country in search_countries]

    filtered_data = [
        row for row in data
        if row['Country Name'] in search_countries and row['2015'] and row['2019']
    ]

    if not filtered_data:
        print("Дані для заданих країн не знайдено.")
        return

    fieldnames = ['Country Name', '2015', '2019']
    write_csv(output_file, filtered_data, fieldnames)

if __name__ == "__main__":
    main()
