import re

def clean_data(data):
    return list(map(lambda x: x.strip().lower(), data.split(',')))

def filter_emails(emails):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'
    valid_emails = filter(lambda x: re.match(pattern, x), emails.split())
    return list(valid_emails)

def extract_keywords(text, min_length=4):
    return list(filter(lambda x: len(x) > min_length, text.split()))

def process_text(text):
    return list(filter(lambda x: x.strip(), map(lambda x: ''.join(filter(str.isalnum, x)).lower(), text.split())))

def normalize_data(numbers):
    values = list(map(float, numbers.split(',')))
    max_value = max(values)
    return [round(x / max_value, 3) for x in values]

def concatenate_strings(data, separator):
    return ''.join(data.split(separator))

def sum_numeric_strings(numbers):
    valid_numbers = [int(x) for x in numbers.split(',') if x.strip().isdigit()]
    return sum(valid_numbers)

def filter_numbers(string, threshold):
    numbers = re.findall(r'\d+', string)
    filtered_numbers = [int(num) for num in numbers if int(num) > threshold]
    return filtered_numbers

def map_to_squares(numbers):
    return list(map(lambda x: int(x) ** 2, numbers.split(',')))

def reverse_strings(words):
    return [word[::-1] for word in words.split(',')]

# Testing the functions
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
