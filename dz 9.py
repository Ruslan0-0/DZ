import re
from collections import Counter
import os
import json
import csv
import shutil


# Получение имени ОС
os_name = os.name
print("Имя ОС:", os_name)

# Получение текущего пути
current_path = os.getcwd()
print("Текущий путь:", current_path)

# Создание папок для каждого типа файлов
file_types = set()
for file_name in os.listdir(current_path):
    _, extension = os.path.splitext(file_name)
    file_types.add(extension)

for file_type in file_types:
    folder = current_path + "/" + file_type[1:]
    os.makedirs(folder, exist_ok=True)

# Перемещение файлов в соответствующие папки
file_moves = {}
for file_name in os.listdir(current_path):
    if os.path.isfile(file_name):
        _, extension = os.path.splitext(file_name)
        if extension != '':
            source = current_path + "/" + file_name
            destination = current_path + "/" + extension[1:] + "/" + file_name
            shutil.move(source, destination)

            if extension not in file_moves:
                file_moves[extension] = 1
            else:
                file_moves[extension] += 1

# Вывод информации о перемещенных файлах
for file_type, count in file_moves.items():
    folder = current_path + "/" + file_type[1:]
    total_size = sum(os.path.getsize(os.path.join(folder, f)) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)))
    print(f"В папке с {file_type[1:]} файлами перемещено {count} файлов, их суммарный размер - {total_size} гигабайт")



#  Заменяем на N фио
text = "Подсудимая Эверт-Колокольцева Елизавета Александровна в судебном заседании вину признала в полном обьеме."

print(re.sub(r'[А-ЯЁ]\w*'r'(?:-[А-ЯЁ]\w*)?'r'(?: [А-ЯЁ]\w*){2}', 'N', text))

часто встречаемое слово

def word(line):
    # Разделить строку на слова
    words = line.split()

    # Подсчитать количество каждого слова
    word_counts = Counter(words)

    # Найти самое часто встречаемое слово и его количество
    most_word, count = word_counts.most_common(1)[0]

    return most_word, count


# Считать текст из файла
with open('output.txt', 'r') as file:
    lines = file.readlines()

# Обработать каждую строку и записать результаты в новый файл
with open('output.txt', 'w') as file:
    for line in lines:
        line = line.strip()  # Удалить лишние пробелы в начале и конце строки
        if line != '':
            most_word, count = word(line)
            file.write(f'{most_word}: {count}\n')

Запрещенные слова

def censor_text_file(filename):
    with open("stop_words.txt", 'r') as stop_words_file: #файл с запрещенными словами
        stop_words = stop_words_file.read().lower().split()
        with open(filename, "r") as file:
            content = file.read()
        for word in stop_words:
            content = content.lower().replace(word, "*" * len(word))
        print(content)
filename = input("Введите название файла: ")
censor_text_file(filename)

Оценки ниже 3

def klass(filenames):
    with open(filenames, "r") as file:
    # Чтение содержимого файла построчно
        lines = file.readlines()

    for line in lines:
        # Разделение строки на фамилию имя и оценку
        data = line.strip().split()
        name = " ".join(data[:-1])
        grade = int(data[-1])

    # Вывод учащихся с оценкой меньше трех баллов
        if grade < 3:
            print(f"{name}: {grade} балл")


filenames = input("Введите название файла: ")
klass(filenames)

  Cумма чисел

def summ_filed(file_name):
    total_sum = 0

    pattern = r'\d+'  # Регулярное выражение для поиска чисел

    with open(file_name, 'r') as file:
        content = file.read()
        numbers = re.findall(pattern, content)  # находим все числа в содержимом файла

        for number in numbers:
            total_sum += int(number)  # преобразуем число из строки в целое число

    return total_sum

file_name = 'file.txt'
total_sum = summ_filed(file_name)
print('Сумма всех чисел : ', total_sum)

Шифрование по Цезарю
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result

def encrypt_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        lines = content.split('\n')

        encrypted_lines = []
        for i, line in enumerate(lines):
            shift = i + 1
            encrypted_line = caesar_cipher(line, shift)
            encrypted_lines.append(encrypted_line)

    encrypted_content = '\n'.join(encrypted_lines)

    encrypted_file_name = 'encrypted_' + file_name
    with open(encrypted_file_name, 'w') as encrypted_file:
        encrypted_file.write(encrypted_content)

# Пример использования
file_name = 'ferrari.txt'
encrypt_file(file_name)
print("Файл успешно зашифрован.")

# JSON CSV

#Создаем файл
def read_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data
# Создаем файл CSV
def convert_to_csv(data, csv_file):
    keys = data[0].keys()
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

# Добавление сотрудника
def add_employee_to_json(data, employee_data):
    data.append(employee_data)
    return data

def add_employee_to_csv(csv_file, employee_data):
    with open(csv_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=employee_data.keys())
        writer.writerow(employee_data)

# Поиск по имени
def search_employee_be_name(data, name):
    for employee in data:
        if employee["name"] == name:
            return employee
        return None
# Фильтр по языку программирования
def filter_by_language(data, languages):
    filtered_employees = []
    for employee in data:
        if languages in employee['programming_languages']:
            filtered_employees.append(employee)
    return filtered_employees

# Фильтр по дню рождения
def filter_by_birth_year(data, birth_year):
    filtered_employees = []
    for employee in data:
        if employee['birth_year'] < birth_year:
            filtered_employees.append(employee)
    return filtered_employees






def user_menu():
    data = read_json("employees.json")
    while True:
        print("Меню:")
        print("1. Вывести информацию об одном сотруднике по имени")
        print("2. Фильтр по языку программирования")
        print("3. Фильтр по году рождения")
        print("4. Добавить информацию о новом сотруднике в JSON-файл")
        print("5. Добавить информацию о новом сотруднике в CSV-файл")
        print("6. Выйти")

        choice = input("Введите число соответствующее действию: ")

        if choice == '1':
            name = input("Введите имя сотрудника: ")
            employee = search_employee_be_name(data, name)
            if employee:
                print(employee)
            else:
                print("Сотрудник с таким именем не найден")
        elif choice == '2':
            languages = input("Введите язык программирования: ")
            filtered_employees = filter_by_language(data, languages)
            if filtered_employees:
                for employee in filtered_employees:
                    print(employee)
            else:
                print("Ни один сотрудник не владеет указанным языком программирования")
        elif choice == '3':
            birthday = int(input("Введите год рождения: "))
            filtered_employees = filter_by_birth_year(data, birthday)
            if filtered_employees:
                for employee in filtered_employees:
                    print(employee)
            else:
                print("Ни один сотрудник не родился раньше указанного года")
        elif choice == '4':
            # Добавление информации о новом сотруднике в JSON-файл
            employee_data = {}
            # Добавление информации о новом сотруднике в JSON-файл
            employee_data["name"] = input("Name: ")
            employee_data["position"] = input("Должность: ")
            employee_data["salary"] = input("Зарплата: ")

            add_employee_to_json(data, employee_data)

        elif choice == '5':
            employee_data = {}
            # Добавление информации о новом сотруднике в CSV-файл
            employee_data["name"] = input("Name: ")
            employee_data["position"] = input("Должность: ")
            employee_data["salary"] = input("Зарплата: ")

            add_employee_to_csv("employees.csv", employee_data)
            print("Информация добавлена в  СSV файл")
        elif choice == '6':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


user_menu()
