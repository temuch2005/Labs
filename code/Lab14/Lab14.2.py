import pandas as pd
import matplotlib.pyplot as plt

file_path = "myData.csv"
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    print("Файл не знайдено. Перевірте шлях до файлу.")
    exit()

data['Year'] = data['Year'].astype(int)

ukraine_data = data[data['Country'] == 'Ukraine']
usa_data = data[data['Country'] == 'United States']

years = ukraine_data['Year']
ukraine_values = ukraine_data['Value']
usa_values = usa_data['Value']

plt.figure(figsize=(10, 6))
plt.plot(years, ukraine_values, label='Ukraine', color='green', linewidth=2)
plt.plot(years, usa_values, label='United States', color='red', linewidth=2)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Indicator Value", fontsize=12)
plt.title("Indicator Dynamics for Ukraine and USA", fontsize=14)
plt.xticks(years, rotation=45)
plt.legend()
plt.grid(True)
plt.show()

country = input("Введіть назву країни (Ukraine / United States): ").strip()
if country not in data['Country'].unique():
    print("Немає даних для цієї країни.")
    exit()

country_data = data[data['Country'] == country]
years = country_data['Year']
values = country_data['Value']

plt.figure(figsize=(10, 6))
plt.bar(years, values, color='green', alpha=0.7)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Indicator Value", fontsize=12)
plt.title(f"Indicator Values for {country}", fontsize=14)
plt.xticks(years, rotation=45)
plt.show()
