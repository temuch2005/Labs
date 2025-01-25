import pandas as pd

def display_all_students(data):
    print("\nВсі учні в словнику:")
    for key, value in data.items():
        print(f"{key}: {value}")

def convert_to_dataframe(data):
    df = pd.DataFrame.from_dict(data, orient='index')
    print("\nDataFrame створений зі словника:")
    print(df)
    return df

def perform_aggregation_and_grouping(df):
    grouped = df.groupby('Номер школи').agg({'Клас': 'count'}).rename(columns={'Клас': 'Кількість учнів'})
    print("\nКількість учнів у кожній школі:")
    print(grouped)

    average_class = df.groupby('Номер школи')['Клас'].mean().reset_index(name='Середній клас')
    print("\nСередній клас учнів у кожній школі:")
    print(average_class)

    max_class = df.groupby('Номер школи')['Клас'].max().reset_index(name='Максимальний клас')
    print("\nМаксимальний клас учнів у кожній школі:")
    print(max_class)

def main():
    students = {
        1: {"Прізвище": "Іваненко", "Ім'я": "Іван", "Адреса": "вул. Шевченка, 10", "Номер школи": 5, "Клас": 11},
        2: {"Прізвище": "Петренко", "Ім'я": "Петро", "Адреса": "вул. Грушевського, 20", "Номер школи": 3, "Клас": 9},
        3: {"Прізвище": "Сидоренко", "Ім'я": "Олена", "Адреса": "вул. Франка, 30", "Номер школи": 5, "Клас": 10},
        4: {"Прізвище": "Коваленко", "Ім'я": "Анна", "Адреса": "вул. Січових Стрільців, 40", "Номер школи": 1,
            "Клас": 8},
        5: {"Прізвище": "Шевченко", "Ім'я": "Михайло", "Адреса": "вул. Лесі Українки, 50", "Номер школи": 3,
            "Клас": 11},
        6: {"Прізвище": "Гнатенко", "Ім'я": "Олег", "Адреса": "вул. Чорновола, 60", "Номер школи": 2, "Клас": 7},
    }

    display_all_students(students)

    df = convert_to_dataframe(students)

    perform_aggregation_and_grouping(df)

if __name__ == "__main__":
    main()
