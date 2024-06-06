# Lab-15
Лабораторна робота 15: Робота з рядками та списками в Python

Мета роботи:
Метою цієї лабораторної роботи є ознайомлення з методами обробки рядків та списків у мові програмування Python. Очікувані результати включають вміння очищати дані, фільтрувати електронні адреси, виділяти ключові слова, обробляти текстові дані, нормалізувати числові дані та виконувати інші маніпуляції з рядками та списками.

Опис завдання:
Необхідно реалізувати кілька функцій, які виконують різноманітні операції над рядками та списками. Завдання включають очищення даних, фільтрацію електронних адрес, виділення ключових слів, нормалізацію чисел, конкатенацію рядків, підсумовування числових рядків, фільтрацію чисел, піднесення чисел до квадрату та реверсування рядків.

Виконання роботи:
Кожне завдання реалізовано у вигляді окремої функції, яка приймає вхідні параметри та повертає результат. Усі функції містяться в одному файлі main.py.

Код програми:
import re

# Task 1: Clean Data
def clean_data(data):
    return list(map(lambda x: x.strip().lower(), data.split(',')))

# Task 2: Filter Emails
def filter_emails(emails):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'
    valid_emails = filter(lambda x: re.match(pattern, x), emails.split())
    return list(valid_emails)

# Task 3: Extract Keywords
def extract_keywords(text, min_length=4):
    return list(filter(lambda x: len(x) > min_length, text.split()))

# Task 4: Process Text
def process_text(text):
    return list(filter(lambda x: x.strip(), map(lambda x: ''.join(filter(str.isalnum, x)).lower(), text.split())))

# Task 5: Normalize Data
def normalize_data(numbers):
    values = list(map(float, numbers.split(',')))
    max_value = max(values)
    return [round(x / max_value, 3) for x in values]

# Task 6: Concatenate Strings
def concatenate_strings(data, separator):
    return ''.join(data.split(separator))

# Task 7: Sum Numeric Strings
def sum_numeric_strings(numbers):
    valid_numbers = [int(x) for x in numbers.split(',') if x.strip().isdigit()]
    return sum(valid_numbers)

# Task 8: Filter Numbers
def filter_numbers(string, threshold):
    numbers = re.findall(r'\d+', string)
    filtered_numbers = [int(num) for num in numbers if int(num) > threshold]
    return filtered_numbers

# Task 9: Map to Squares
def map_to_squares(numbers):
    return list(map(lambda x: int(x) ** 2, numbers.split(',')))

# Task 10: Reverse Strings
def reverse_strings(words):
    return [word[::-1] for word in words.split(',')]

# Testing the functions
if __name__ == "__main__":
    data = " Apple, Banana , orange "
    cleaned = clean_data(data)
    print(cleaned)  # ['apple', 'banana', 'orange']

    emails = "mail us @email.com test@example.com and invalid-email.com.djwd with example@test.co"
    valid_emails = filter_emails(emails)
    print(valid_emails)  # ['test@example.com', 'example@test.co']

    words = "apple pear banana kiwi"
    filtered_words = extract_keywords(words, 4)
    print(filtered_words)  # ['apple', 'banana']

    texts = " Hello! , Yes? , No. , "
    processed_texts = process_text(texts)
    print(processed_texts)  # ['hello', 'yes', 'no']

    numbers = "10, 20,30"
    normalized_numbers = normalize_data(numbers)
    print(normalized_numbers)  # [0.333, 0.667, 1.0]

    data = "hello*world*again"
    concatenated = concatenate_strings(data, '*')
    print(concatenated)  # 'helloworldagain'

    numbers = "1, 2, test, 3, 4"
    total_sum = sum_numeric_strings(numbers)
    print(total_sum)  # 10

    numbers = "10, test30, 40"
    filtered = filter_numbers(numbers, 25)
    print(filtered)  # [30, 40]

    numbers = "1, 2, 3, 4"
    squared_numbers = map_to_squares(numbers)
    print(squared_numbers)  # [1, 4, 9, 16]

    words = "apple,banana,carrot"
    reversed_words = reverse_strings(words)
    print(reversed_words)  # ['elppa', 'ananab', 'torrac']
    
Проект організовано у вигляді папки з наступними файлами:

main.py: Основний код програми.
README.md: Файл з детальним поясненням проекту.
Опис кожного файлу та його призначення:
main.py: Містить реалізацію всіх функцій згідно з завданням.
README.md: Містить загальний опис проекту, мету, інструкції з використання та приклади використання функцій.
Опис основних функцій та методів з поясненням їх роботи:
clean_data(data): Очищає дані, видаляючи зайві пробіли та переводячи текст у нижній регістр.
filter_emails(emails): Фільтрує валідні електронні адреси з рядка.
extract_keywords(text, min_length): Виділяє ключові слова з тексту, довжина яких перевищує вказану мінімальну.
process_text(text): Обробляє текст, видаляючи небуквені символи та перетворюючи на нижній регістр.
normalize_data(numbers): Нормалізує числові дані, ділячи кожне число на максимальне значення у списку.
concatenate_strings(data, separator): Конкатенує рядки, розділені вказаним сепаратором.
sum_numeric_strings(numbers): Повертає суму числових рядків.
filter_numbers(string, threshold): Фільтрує числа з рядка, залишаючи лише ті, що перевищують вказаний поріг.
map_to_squares(numbers): Повертає список квадратів чисел.
reverse_strings(words): Повертає список реверсованих слів.

Результати:
Отримані результати демонструють правильність роботи реалізованих функцій. Кожна функція повертає очікувані результати при різних вхідних даних.

Приклади виводу програми:
clean_data(" Apple, Banana , orange ") повертає ['apple', 'banana', 'orange']
filter_emails("mail us @email.com test@example.com and invalid-email.com.djwd with example@test.co") повертає ['test@example.com', 'example@test.co']
extract_keywords("apple pear banana kiwi", 4) повертає ['apple', 'banana']
process_text(" Hello! , Yes? , No. , ") повертає ['hello', 'yes', 'no']
normalize_data("10, 20,30") повертає [0.333, 0.667, 1.0]
concatenate_strings("hello*world*again", '*') повертає 'helloworldagain'
sum_numeric_strings("1, 2, test, 3, 4") повертає 10
filter_numbers("10, test30, 40", 25) повертає [30, 40]
map_to_squares("1, 2, 3, 4") повертає [1, 4, 9, 16]
reverse_strings("apple,banana,carrot") повертає ['elppa', 'ananab', 'torrac']


Для запуску програми необхідно:Встановити Python версії 3.6 або вище.
