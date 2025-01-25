import json
import matplotlib.pyplot as plt

def read_json_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Помилка: файл {file_name} не знайдено.")
        return []
    except json.JSONDecodeError:
        print(f"Помилка: файл {file_name} має некоректний формат JSON.")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу {file_name}: {e}")
        return []

def build_pie_chart(data):
    class_counts = {}
    for record in data:
        cls = record.get("клас")
        if cls:
            class_counts[cls] = class_counts.get(cls, 0) + 1

    labels = [f"Клас {key}" for key in class_counts.keys()]
    sizes = list(class_counts.values())
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

    plt.figure(figsize=(8, 8))
    plt.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=140,
        wedgeprops={'edgecolor': 'black'}
    )
    plt.title("Розподіл учнів за класами")
    plt.show()

def main():
    input_file = "students.json"
    data = read_json_file(input_file)
    if not data:
        print("Немає даних для побудови кругової діаграми.")
        return
    build_pie_chart(data)

if __name__ == "__main__":
    main()
