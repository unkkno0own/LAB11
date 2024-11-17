import csv

def read_csv(file_path):
    """
    Зчитує вміст .csv файлу.
    """
    try:
        # Використовуємо 'latin1' або 'windows-1251' кодування, або 'errors="ignore"' для ігнорування помилок
        with open(file_path, mode='r', encoding='latin1', errors='ignore') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            return data
    except FileNotFoundError:
        print(f"Помилка: Файл {file_path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
    return None

def write_csv(file_path, data, fieldnames):
    """
    Записує дані у новий .csv файл.
    """
    try:
        # Використовую 'latin1' для запису у файл
        with open(file_path, mode='w', encoding='latin1', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Результати збережено у файл {file_path}.")
    except Exception as e:
        print(f"Сталася помилка при записі у файл: {e}")

def search_countries(data, countries):
    """
    Пошук даних для введених користувачем країн.
    """
    result = []
    for country in countries:
        for row in data:
            if row.get("Country Name", "").strip().lower() == country.strip().lower():
                result.append(row)
                break
    return result

def main():
    # Шлях до вхідного файлу
    input_file = "gdp_per_capita_growth_2019.csv"  # Замість цього вставте шлях до файлу
    output_file = "filtered_countries_gdp.csv"

    # Зчитування вмісту файлу
    data = read_csv(input_file)
    if not data:
        return

    # Виведення вмісту файлу
    print("Вміст файлу:")
    for row in data[:5]:  # Вивести перші 5 рядків для прикладу
        print(row)
    print("...")

    # Введення країн для пошуку
    countries = input("Введіть назви країн через кому: ").split(',')

    # Пошук даних для зазначених країн
    results = search_countries(data, countries)

    # Запис результатів у новий .csv файл
    if results:
        fieldnames = data[0].keys()  # Заголовки колонок
        write_csv(output_file, results, fieldnames)
    else:
        print("Дані для зазначених країн не знайдено.")

if __name__ == "__main__":
    main()
