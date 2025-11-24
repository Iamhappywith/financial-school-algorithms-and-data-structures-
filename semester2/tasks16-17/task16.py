# ЗАДАНИЕ 1-15. ФУНКЦИИ С ПАРАМЕТРАМИ (15 задач)

def task1():
    print("\n=== ЗАДАНИЕ 1 ===")
    
    # а) Функция full_name
    def full_name(first_name, last_name, middle_name=None):
        if middle_name:
            return f"{last_name} {first_name} {middle_name}"
        else:
            return f"{last_name} {first_name}"
    
    print("а) Функция full_name:")
    print("Введите имя:")
    first = input("Имя: ")
    print("Введите фамилию:")
    last = input("Фамилия: ")
    print("Введите отчество (если есть, иначе нажмите Enter):")
    middle = input("Отчество: ").strip()
    
    if middle:
        result1 = full_name(first, last, middle)
    else:
        result1 = full_name(first, last)
    print(f"Результат: '{result1}'")
    
    # б) Функция transform_list
    def transform_list(numbers, transform_function=None):
        if transform_function:
            return [transform_function(x) for x in numbers]
        else:
            return numbers.copy()
    
    print("\nб) Функция transform_list:")
    print("Введите список чисел через пробел:")
    numbers_input = list(map(int, input().split()))
    
    print("Применить преобразование? (y/n):")
    choice = input().lower()
    if choice == 'y':
        print("Введите преобразование (например: x*2, x**2, x+10):")
        transform_code = input()
        try:
            transform_func = eval(f"lambda x: {transform_code}")
            result2 = transform_list(numbers_input, transform_func)
        except:
            print("Ошибка в преобразовании, возвращаем исходный список")
            result2 = transform_list(numbers_input)
    else:
        result2 = transform_list(numbers_input)
    
    print(f"Результат: {result2}")
    
    # в) Функция sum_positive_numbers
    def sum_positive_numbers(*args):
        total = 0
        for num in args:
            if num > 0:
                total += num
        return total
    
    print("\nв) Функция sum_positive_numbers:")
    print("Введите числа через пробел:")
    numbers = list(map(int, input().split()))
    result3 = sum_positive_numbers(*numbers)
    print(f"Сумма положительных чисел: {result3}")
    
    # г) Функция common_keys
    def common_keys(**kwargs):
        if not kwargs:
            return {}
        
        dicts = list(kwargs.values())
        common = dicts[0].copy()
        
        for d in dicts[1:]:
            keys_to_remove = []
            for key in common:
                if key not in d:
                    keys_to_remove.append(key)
            for key in keys_to_remove:
                del common[key]
        
        return common
    
    print("\nг) Функция common_keys:")
    print("Сколько словарей вы хотите ввести?")
    num_dicts = int(input())
    dicts = {}
    
    for i in range(num_dicts):
        print(f"Введите словарь {i+1} в формате 'ключ:значение,ключ:значение':")
        dict_str = input()
        pairs = dict_str.split(',')
        current_dict = {}
        for pair in pairs:
            key, value = pair.split(':')
            current_dict[key.strip()] = value.strip()
        dicts[f'dict{i+1}'] = current_dict
    
    result4 = common_keys(**dicts)
    print(f"Общие ключи: {result4}")
    
    return result1, result2, result3, result4

def task2():
    print("\n=== ЗАДАНИЕ 2 ===")
    
    # а) Функция sort_numbers
    def sort_numbers(numbers, reverse_order=False):
        return sorted(numbers, reverse=reverse_order)
    
    print("а) Функция sort_numbers:")
    print("Введите список чисел через пробел:")
    numbers = list(map(int, input().split()))
    
    print("Сортировать по убыванию? (y/n):")
    reverse_choice = input().lower()
    reverse = reverse_choice == 'y'
    
    result1 = sort_numbers(numbers, reverse)
    print(f"Отсортированный список: {result1}")
    
    # б) Функция uppercase_text
    def uppercase_text(text, separator=' '):
        words = text.split(separator)
        upper_words = [word.upper() for word in words]
        return separator.join(upper_words)
    
    print("\nб) Функция uppercase_text:")
    print("Введите текст:")
    text = input("Текст: ")
    print("Введите разделитель (по умолчанию пробел):")
    sep = input("Разделитель: ").strip()
    
    if sep:
        result2 = uppercase_text(text, sep)
    else:
        result2 = uppercase_text(text)
    
    print(f"Результат: '{result2}'")
    
    # в) Функция multiply_all
    def multiply_all(*args):
        result = 1
        for num in args:
            result *= num
        return result
    
    print("\nв) Функция multiply_all:")
    print("Введите числа через пробел:")
    numbers = list(map(int, input().split()))
    result3 = multiply_all(*numbers)
    print(f"Произведение чисел: {result3}")
    
    # г) Функция filter_strings
    def filter_strings(strings, **criteria):
        result = []
        for s in strings:
            valid = True
            
            if 'min_length' in criteria and len(s) < criteria['min_length']:
                valid = False
            if 'starts_with' in criteria and not s.startswith(criteria['starts_with']):
                valid = False
            if 'ends_with' in criteria and not s.endswith(criteria['ends_with']):
                valid = False
            
            if valid:
                result.append(s)
        
        return result
    
    print("\nг) Функция filter_strings:")
    print("Введите строки через запятую:")
    strings_input = [s.strip() for s in input().split(',')]
    
    criteria = {}
    print("Минимальная длина (если нужна, иначе Enter):")
    min_len = input()
    if min_len:
        criteria['min_length'] = int(min_len)
    
    print("Начинается с (если нужно, иначе Enter):")
    starts = input()
    if starts:
        criteria['starts_with'] = starts
    
    print("Заканчивается на (если нужно, иначе Enter):")
    ends = input()
    if ends:
        criteria['ends_with'] = ends
    
    result4 = filter_strings(strings_input, **criteria)
    print(f"Отфильтрованные строки: {result4}")
    
    return result1, result2, result3, result4

def task3():
    print("\n=== ЗАДАНИЕ 3 ===")
    
    # а) Функция split_string
    def split_string(text, delimiter=' '):
        return text.split(delimiter)
    
    print("а) Функция split_string:")
    print("Введите текст:")
    text = input("Текст: ")
    print("Введите разделитель (по умолчанию пробел):")
    delimiter = input("Разделитель: ").strip()
    
    if delimiter:
        result1 = split_string(text, delimiter)
    else:
        result1 = split_string(text)
    
    print(f"Результат: {result1}")
    
    # б) Функция compare_elements
    def compare_elements(list1, list2, comparison_function=None):
        if comparison_function is None:
            comparison_function = lambda x, y: x == y
        
        result = []
        min_len = min(len(list1), len(list2))
        
        for i in range(min_len):
            if comparison_function(list1[i], list2[i]):
                result.append((list1[i], list2[i]))
        
        return result
    
    print("\nб) Функция compare_elements:")
    print("Введите первый список чисел через пробел:")
    list1 = list(map(int, input().split()))
    print("Введите второй список чисел через пробел:")
    list2 = list(map(int, input().split()))
    
    print("Использовать стандартное сравнение (равенство)? (y/n):")
    choice = input().lower()
    if choice == 'y':
        result2 = compare_elements(list1, list2)
    else:
        print("Введите условие сравнения (например: x+y>5, x*y<10):")
        condition = input()
        try:
            comp_func = eval(f"lambda x, y: {condition}")
            result2 = compare_elements(list1, list2, comp_func)
        except:
            print("Ошибка в условии, используем стандартное сравнение")
            result2 = compare_elements(list1, list2)
    
    print(f"Пары элементов: {result2}")
    
    # в) Функция count_unique_chars
    def count_unique_chars(*args):
        all_chars = set()
        for s in args:
            all_chars.update(s)
        return len(all_chars)
    
    print("\nв) Функция count_unique_chars:")
    print("Введите строки через запятую:")
    strings = [s.strip() for s in input().split(',')]
    result3 = count_unique_chars(*strings)
    print(f"Количество уникальных символов: {result3}")
    
    # г) Функция common_elements
    def common_elements(*lists):
        if not lists:
            return []
        
        common = set(lists[0])
        for lst in lists[1:]:
            common = common.intersection(set(lst))
        
        return list(common)
    
    print("\nг) Функция common_elements:")
    print("Сколько списков вы хотите ввести?")
    num_lists = int(input())
    lists = []
    
    for i in range(num_lists):
        print(f"Введите список {i+1} через пробел:")
        current_list = input().split()
        lists.append(current_list)
    
    result4 = common_elements(*lists)
    print(f"Общие элементы: {result4}")
    
    return result1, result2, result3, result4

def task4():
    print("\n=== ЗАДАНИЕ 4 ===")
    
    # а) Функция calculate
    def calculate(a, b, operation='add'):
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
        elif operation == 'divide':
            if b == 0:
                return "Ошибка: деление на ноль!"
            return a / b
        else:
            return "Неизвестная операция"
    
    print("а) Функция calculate:")
    print("Введите первое число:")
    a = float(input("a = "))
    print("Введите второе число:")
    b = float(input("b = "))
    
    print("Выберите операцию (add, subtract, multiply, divide):")
    op = input("Операция: ").strip().lower()
    
    if op in ['add', 'subtract', 'multiply', 'divide']:
        result1 = calculate(a, b, op)
    else:
        result1 = calculate(a, b)
    
    print(f"Результат: {result1}")
    
    # б) Функция modify_strings
    def modify_strings(strings, case=None):
        if case == 'upper':
            return [s.upper() for s in strings]
        elif case == 'lower':
            return [s.lower() for s in strings]
        else:
            return strings.copy()
    
    print("\nб) Функция modify_strings:")
    print("Введите строки через запятую:")
    strings = [s.strip() for s in input().split(',')]
    
    print("Изменить регистр? (upper/lower/none):")
    case_choice = input().lower()
    
    if case_choice in ['upper', 'lower']:
        result2 = modify_strings(strings, case_choice)
    else:
        result2 = modify_strings(strings)
    
    print(f"Результат: {result2}")
    
    # в) Функция average
    def average(*args):
        if not args:
            return 0
        return sum(args) / len(args)
    
    print("\nв) Функция average:")
    print("Введите числа через пробел:")
    numbers = list(map(float, input().split()))
    result3 = average(*numbers)
    print(f"Среднее значение: {result3}")
    
    # г) Функция merge_dictionaries
    def merge_dictionaries(base_dict, **additional_dicts):
        result = base_dict.copy()
        for d in additional_dicts.values():
            result.update(d)
        return result
    
    print("\nг) Функция merge_dictionaries:")
    print("Введите базовый словарь в формате 'ключ:значение,ключ:значение':")
    base_str = input()
    base_pairs = base_str.split(',')
    base_dict = {}
    for pair in base_pairs:
        key, value = pair.split(':')
        base_dict[key.strip()] = value.strip()
    
    print("Сколько дополнительных словарей?")
    num_dicts = int(input())
    add_dicts = {}
    
    for i in range(num_dicts):
        print(f"Введите словарь {i+1} в формате 'ключ:значение,ключ:значение':")
        dict_str = input()
        pairs = dict_str.split(',')
        current_dict = {}
        for pair in pairs:
            key, value = pair.split(':')
            current_dict[key.strip()] = value.strip()
        add_dicts[f'dict{i+1}'] = current_dict
    
    result4 = merge_dictionaries(base_dict, **add_dicts)
    print(f"Объединенный словарь: {result4}")
    
    return result1, result2, result3, result4

def task5():
    print("\n=== ЗАДАНИЕ 5 ===")
    
    # а) Функция filter_items
    def filter_items(items, condition=None):
        if condition is None:
            return items.copy()
        return [item for item in items if condition(item)]
    
    print("а) Функция filter_items:")
    print("Введите список чисел через пробел:")
    items = list(map(int, input().split()))
    
    print("Применить фильтр? (y/n):")
    choice = input().lower()
    if choice == 'y':
        print("Введите условие фильтра (например: x>3, x%2==0):")
        condition_str = input()
        try:
            cond_func = eval(f"lambda x: {condition_str}")
            result1 = filter_items(items, cond_func)
        except:
            print("Ошибка в условии, возвращаем исходный список")
            result1 = filter_items(items)
    else:
        result1 = filter_items(items)
    
    print(f"Результат: {result1}")
    
    # б) Функция merge_and_filter
    def merge_and_filter(list1, list2, filter_function=None):
        merged = list1 + list2
        if filter_function is None:
            return merged
        return [item for item in merged if filter_function(item)]
    
    print("\nб) Функция merge_and_filter:")
    print("Введите первый список через пробел:")
    list1 = list(map(int, input().split()))
    print("Введите второй список через пробел:")
    list2 = list(map(int, input().split()))
    
    print("Применить фильтр? (y/n):")
    choice = input().lower()
    if choice == 'y':
        print("Введите условие фильтра (например: x%2==0, x>5):")
        filter_str = input()
        try:
            filter_func = eval(f"lambda x: {filter_str}")
            result2 = merge_and_filter(list1, list2, filter_func)
        except:
            print("Ошибка в условии, возвращаем объединенный список")
            result2 = merge_and_filter(list1, list2)
    else:
        result2 = merge_and_filter(list1, list2)
    
    print(f"Результат: {result2}")
    
    # в) Функция common_in_all
    def common_in_all(*lists):
        if not lists:
            return []
        
        common = set(lists[0])
        for lst in lists[1:]:
            common = common.intersection(set(lst))
        
        return list(common)
    
    print("\nв) Функция common_in_all:")
    print("Сколько списков вы хотите ввести?")
    num_lists = int(input())
    lists = []
    
    for i in range(num_lists):
        print(f"Введите список {i+1} через пробел:")
        current_list = input().split()
        lists.append(current_list)
    
    result3 = common_in_all(*lists)
    print(f"Элементы, присутствующие во всех списках: {result3}")
    
    # г) Функция find_primes
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def find_primes(*numbers):
        return [n for n in numbers if is_prime(n)]
    
    print("\nг) Функция find_primes:")
    print("Введите числа через пробел:")
    numbers = list(map(int, input().split()))
    result4 = find_primes(*numbers)
    print(f"Простые числа: {result4}")
    
    return result1, result2, result3, result4

def task6():
    print("\n=== ЗАДАНИЕ 6 ===")
    
    # а) Функция word_count
    def word_count(text, separator=' '):
        words = text.split(separator)
        count_dict = {}
        for word in words:
            count_dict[word] = count_dict.get(word, 0) + 1
        return count_dict
    
    print("а) Функция word_count:")
    print("Введите текст:")
    text = input("Текст: ")
    print("Введите разделитель (по умолчанию пробел):")
    sep = input("Разделитель: ").strip()
    
    if sep:
        result1 = word_count(text, sep)
    else:
        result1 = word_count(text)
    
    print(f"Количество слов: {result1}")
    
    # б) Функция filter_numbers
    def filter_numbers(numbers, exclude_multiples_of=2):
        return [n for n in numbers if n % exclude_multiples_of != 0]
    
    print("\nб) Функция filter_numbers:")
    print("Введите список чисел через пробел:")
    numbers = list(map(int, input().split()))
    
    print("Введите число для исключения кратных (по умолчанию 2):")
    exclude_input = input().strip()
    if exclude_input:
        exclude = int(exclude_input)
    else:
        exclude = 2
    
    result2 = filter_numbers(numbers, exclude)
    print(f"Числа, не кратные {exclude}: {result2}")
    
    # в) Функция merge_and_sort_keys
    def merge_and_sort_keys(*dicts):
        merged = {}
        for d in dicts:
            for key, value in d.items():
                if key not in merged or value > merged[key]:
                    merged[key] = value
        
        sorted_keys = sorted(merged.keys(), key=lambda k: merged[k], reverse=True)
        return sorted_keys
    
    print("\nв) Функция merge_and_sort_keys:")
    print("Сколько словарей вы хотите ввести?")
    num_dicts = int(input())
    dicts = []
    
    for i in range(num_dicts):
        print(f"Введите словарь {i+1} в формате 'ключ:число,ключ:число':")
        dict_str = input()
        pairs = dict_str.split(',')
        current_dict = {}
        for pair in pairs:
            key, value = pair.split(':')
            current_dict[key.strip()] = int(value.strip())
        dicts.append(current_dict)
    
    result3 = merge_and_sort_keys(*dicts)
    print(f"Ключи, отсортированные по убыванию значений: {result3}")
    
    # г) Функция sum_non_negative
    def sum_non_negative(*args):
        total = 0
        for num in args:
            if num >= 0:
                total += num
        return total
    
    print("\nг) Функция sum_non_negative:")
    print("Введите числа через пробел:")
    numbers = list(map(int, input().split()))
    result4 = sum_non_negative(*numbers)
    print(f"Сумма неотрицательных чисел: {result4}")
    
    return result1, result2, result3, result4

def task7():
    print("\n=== ЗАДАНИЕ 7 ===")
    
    # а) Функция join_strings
    def join_strings(strings, delimiter=','):
        return delimiter.join(strings)
    
    print("а) Функция join_strings:")
    print("Введите строки через запятую:")
    strings = [s.strip() for s in input().split(',')]
    
    print("Введите разделитель (по умолчанию запятая):")
    delimiter = input("Разделитель: ").strip()
    
    if delimiter:
        result1 = join_strings(strings, delimiter)
    else:
        result1 = join_strings(strings)
    
    print(f"Результат: '{result1}'")
    
    # б) Функция combine_lists
    def combine_lists(list1, list2, join_str=''):
        result = []
        min_len = min(len(list1), len(list2))
        for i in range(min_len):
            result.append(f"{list1[i]}{join_str}{list2[i]}")
        return result
    
    print("\nб) Функция combine_lists:")
    print("Введите первый список через пробел:")
    list1 = input().split()
    print("Введите второй список через пробел:")
    list2 = input().split()
    
    print("Введите строку для соединения (по умолчанию пустая):")
    join_str = input("Строка соединения: ")
    
    result2 = combine_lists(list1, list2, join_str)
    print(f"Результат: {result2}")
    
    # в) Функция unique_values
    def unique_values(*args):
        return list(set(args))
    
    print("\nв) Функция unique_values:")
    print("Введите значения через пробел:")
    values = input().split()
    result3 = unique_values(*values)
    print(f"Уникальные значения: {result3}")
    
    # г) Функция reverse_concatenate
    def reverse_concatenate(*args):
        return ' '.join(reversed(args))
    
    print("\nг) Функция reverse_concatenate:")
    print("Введите строки через пробел:")
    strings = input().split()
    result4 = reverse_concatenate(*strings)
    print(f"Результат: '{result4}'")
    
    return result1, result2, result3, result4

def task8():
    print("\n=== ЗАДАНИЕ 8 ===")
    
    # а) Функция pair_and_filter
    def pair_and_filter(list1, list2, filter_function=None):
        pairs = []
        for x in list1:
            for y in list2:
                if filter_function is None or filter_function(x, y):
                    pairs.append((x, y))
        return pairs
    
    print("а) Функция pair_and_filter:")
    print("Введите первый список через пробел:")
    list1 = list(map(int, input().split()))
    print("Введите второй список через пробел:")
    list2 = list(map(int, input().split()))
    
    print("Применить фильтр? (y/n):")
    choice = input().lower()
    if choice == 'y':
        print("Введите условие фильтра (например: x+y>5, x*y<10):")
        filter_str = input()
        try:
            filter_func = eval(f"lambda x, y: {filter_str}")
            result1 = pair_and_filter(list1, list2, filter_func)
        except:
            print("Ошибка в условии, возвращаем все пары")
            result1 = pair_and_filter(list1, list2)
    else:
        result1 = pair_and_filter(list1, list2)
    
    print(f"Пары элементов: {result1}")
    
    # б) Функция concat_or_upper
    def concat_or_upper(strings, uppercase=False):
        result = ' '.join(strings)
        if uppercase:
            return result.upper()
        else:
            return result
    
    print("\nб) Функция concat_or_upper:")
    print("Введите строки через запятую:")
    strings = [s.strip() for s in input().split(',')]
    
    print("Преобразовать в верхний регистр? (y/n):")
    upper_choice = input().lower()
    upper = upper_choice == 'y'
    
    result2 = concat_or_upper(strings, upper)
    print(f"Результат: '{result2}'")
    
    # в) Функция filter_uppercase_strings
    def filter_uppercase_strings(strings):
        return [s for s in strings if s.isupper()]
    
    print("\nв) Функция filter_uppercase_strings:")
    print("Введите строки через запятую:")
    strings = [s.strip() for s in input().split(',')]
    result3 = filter_uppercase_strings(strings)
    print(f"Строки в верхнем регистре: {result3}")
    
    # г) Функция unique_sorted_elements
    def unique_sorted_elements(*lists):
        all_elements = set()
        for lst in lists:
            all_elements.update(lst)
        return sorted(all_elements)
    
    print("\nг) Функция unique_sorted_elements:")
    print("Сколько списков вы хотите ввести?")
    num_lists = int(input())
    lists = []
    
    for i in range(num_lists):
        print(f"Введите список {i+1} через пробел:")
        current_list = input().split()
        lists.append(current_list)
    
    result4 = unique_sorted_elements(*lists)
    print(f"Уникальные отсортированные элементы: {result4}")
    
    return result1, result2, result3, result4

def task9():
    print("\n=== ЗАДАНИЕ 9 ===")
    
    # а) Функция capitalize_words
    def capitalize_words(text, separator=' '):
        words = text.split(separator)
        capitalized_words = [word.capitalize() for word in words]
        return separator.join(capitalized_words)
    
    print("а) Функция capitalize_words:")
    print("Введите текст:")
    text = input("Текст: ")
    print("Введите разделитель (по умолчанию пробел):")
    sep = input("Разделитель: ").strip()
    
    if sep:
        result1 = capitalize_words(text, sep)
    else:
        result1 = capitalize_words(text)
    
    print(f"Результат: '{result1}'")
    
    # б) Функция filter_elements
    def filter_elements(list1, list2, filter_function=None):
        combined = list1 + list2
        if filter_function is None:
            return combined
        return [item for item in combined if filter_function(item)]
    
    print("\nб) Функция filter_elements:")
    print("Введите первый список через пробел:")
    list1 = list(map(int, input().split()))
    print("Введите второй список через пробел:")
    list2 = list(map(int, input().split()))
    
    print("Применить фильтр? (y/n):")
    choice = input().lower()
    if choice == 'y':
        print("Введите условие фильтра (например: x>3, x%2==0):")
        filter_str = input()
        try:
            filter_func = eval(f"lambda x: {filter_str}")
            result2 = filter_elements(list1, list2, filter_func)
        except:
            print("Ошибка в условии, возвращаем все элементы")
            result2 = filter_elements(list1, list2)
    else:
        result2 = filter_elements(list1, list2)
    
    print(f"Результат: {result2}")
    
    # в) Функция merge_dictionaries
    def merge_dictionaries(*dicts):
        result = {}
        for d in dicts:
            result.update(d)
        return result
    
    print("\nв) Функция merge_dictionaries:")
    print("Сколько словарей вы хотите ввести?")
    num_dicts = int(input())
    dicts = []
    
    for i in range(num_dicts):
        print(f"Введите словарь {i+1} в формате 'ключ:значение,ключ:значение':")
        dict_str = input()
        pairs = dict_str.split(',')
        current_dict = {}
        for pair in pairs:
            key, value = pair.split(':')
            current_dict[key.strip()] = value.strip()
        dicts.append(current_dict)
    
    result3 = merge_dictionaries(*dicts)
    print(f"Объединенный словарь: {result3}")
    
    # г) Функция unique_keys
    def unique_keys(*dicts):
        key_count = {}
        for d in dicts:
            for key in d:
                key_count[key] = key_count.get(key, 0) + 1
        
        result = {}
        for d in dicts:
            for key, value in d.items():
                if key_count[key] == 1:
                    result[key] = value
        return result
    
    print("\nг) Функция unique_keys:")
    print("Сколько словарей вы хотите ввести?")
    num_dicts = int(input())
    dicts = []
    
    for i in range(num_dicts):
        print(f"Введите словарь {i+1} в формате 'ключ:значение,ключ:значение':")
        dict_str = input()
        pairs = dict_str.split(',')
        current_dict = {}
        for pair in pairs:
            key, value = pair.split(':')
            current_dict[key.strip()] = value.strip()
        dicts.append(current_dict)
    
    result4 = unique_keys(*dicts)
    print(f"Уникальные ключи: {result4}")
    
    return result1, result2, result3, result4

def task10():
    print("\n=== ЗАДАНИЕ 10 ===")
    
    # а) Функция filter_numbers
    def filter_numbers(numbers, condition=None):
        if condition is None:
            return numbers.copy()
        return [n for n in numbers if condition(n)]
    
    print("а) Функция filter_numbers:")
    print("Введите список чисел через пробел:")
    numbers = list(map(int, input().split()))
    
    print("Применить условие? (y/n):")
    choice = input().lower()
    if choice == 'y':
        print("Введите условие (например: x%2==0, x>5):")
        condition_str = input()
        try:
            cond_func = eval(f"lambda x: {condition_str}")
            result1 = filter_numbers(numbers, cond_func)
        except:
            print("Ошибка в условии, возвращаем исходный список")
            result1 = filter_numbers(numbers)
    else:
        result1 = filter_numbers(numbers)
    
    print(f"Результат: {result1}")
    
    # б) Функция transform_numbers
    def transform_numbers(numbers, transform_function=None):
        if transform_function is None:
            return numbers.copy()
        return [transform_function(n) for n in numbers]
    
    print("\nб) Функция transform_numbers:")
    print("Введите список чисел через пробел:")
    numbers = list(map(int, input().split()))
    
    print("Применить преобразование? (y/n):")
    choice = input().lower()
    if choice == 'y':
        print("Введите преобразование (например: x**2, x*3, x+10):")
        transform_str = input()
        try:
            transform_func = eval(f"lambda x: {transform_str}")
            result2 = transform_numbers(numbers, transform_func)
        except:
            print("Ошибка в преобразовании, возвращаем исходный список")
            result2 = transform_numbers(numbers)
    else:
        result2 = transform_numbers(numbers)
    
    print(f"Результат: {result2}")
    
    # в) Функция cube_numbers
    def cube_numbers(*lists):
        result = []
        for lst in lists:
            for num in lst:
                result.append(num ** 3)
        return result
    
    print("\nв) Функция cube_numbers:")
    print("Сколько списков вы хотите ввести?")
    num_lists = int(input())
    lists = []
    
    for i in range(num_lists):
        print(f"Введите список {i+1} чисел через пробел:")
        current_list = list(map(int, input().split()))
        lists.append(current_list)
    
    result3 = cube_numbers(*lists)
    print(f"Кубы чисел: {result3}")
    
    # г) Функция product_non_zero
    def product_non_zero(*args):
        result = 1
        has_non_zero = False
        for num in args:
            if num != 0:
                result *= num
                has_non_zero = True
        return result if has_non_zero else 1
    
    print("\nг) Функция product_non_zero:")
    print("Введите числа через пробел:")
    numbers = list(map(int, input().split()))
    result4 = product_non_zero(*numbers)
    print(f"Произведение ненулевых чисел: {result4}")
    
    return result1, result2, result3, result4

def task11():
    print("\n=== ЗАДАНИЕ 11 ===")
    
    # а) Функция format_strings
    def format_strings(strings, separator=' '):
        capitalized = [s.capitalize() for s in strings]
        return separator.join(capitalized)
    
    print("а) Функция format_strings:")
    print("Введите строки через запятую:")
    strings = [s.strip() for s in input().split(',')]
    
    print("Введите разделитель (по умолчанию пробел):")
    sep = input("Разделитель: ").strip()
    
    if sep:
        result1 = format_strings(strings, sep)
    else:
        result1 = format_strings(strings)
    
    print(f"Результат: '{result1}'")
    
    # б) Функция merge_and_sort
    def merge_and_sort(list1, list2, sort_function=None):
        merged = list1 + list2
        if sort_function:
            return sorted(merged, key=sort_function)
        else:
            return sorted(merged)
    
    print("\nб) Функция merge_and_sort:")
    print("Введите первый список чисел через пробел:")
    list1 = list(map(int, input().split()))
    print("Введите второй список чисел через пробел:")
    list2 = list(map(int, input().split()))
    
    print("Использовать специальную сортировку? (y/n):")
    choice = input().lower()
    if choice == 'y':
        print("Введите функцию сортировки (например: -x для убывания, abs(x) для модуля):")
        sort_str = input()
        try:
            sort_func = eval(f"lambda x: {sort_str}")
            result2 = merge_and_sort(list1, list2, sort_func)
        except:
            print("Ошибка в функции сортировки, используем стандартную")
            result2 = merge_and_sort(list1, list2)
    else:
        result2 = merge_and_sort(list1, list2)
    
    print(f"Отсортированный список: {result2}")
    
    # в) Функция concat_all_strings
    def concat_all_strings(*lists):
        all_strings = []
        for lst in lists:
            all_strings.extend(lst)
        return ','.join(all_strings)
    
    print("\nв) Функция concat_all_strings:")
    print("Сколько списков строк вы хотите ввести?")
    num_lists = int(input())
    lists = []
    
    for i in range(num_lists):
        print(f"Введите список {i+1} строк через запятую:")
        current_list = [s.strip() for s in input().split(',')]
        lists.append(current_list)
    
    result3 = concat_all_strings(*lists)
    print(f"Результат: '{result3}'")
    
    # г) Функция unique_sorted_strings
    def unique_sorted_strings(*args):
        unique = set(args)
        return sorted(unique)
    
    print("\nг) Функция unique_sorted_strings:")
    print("Введите строки через пробел:")
    strings = input().split()
    result4 = unique_sorted_strings(*strings)
    print(f"Уникальные отсортированные строки: {result4}")
    
    return result1, result2, result3, result4

def task12():
    print("\n=== ЗАДАНИЕ 12 ===")
    
    # а) Функция combine_lists
    def combine_lists(list1, list2, order='first_second'):
        if order == 'first_second':
            return list1 + list2
        else:
            return list2 + list1
    
    print("а) Функция combine_lists:")
    print("Введите первый список через пробел:")
    list1 = input().split()
    print("Введите второй список через пробел:")
    list2 = input().split()
    
    print("Порядок объединения (first_second/second_first):")
    order_choice = input().strip().lower()
    
    if order_choice == 'second_first':
        result1 = combine_lists(list1, list2, order_choice)
    else:
        result1 = combine_lists(list1, list2)
    
    print(f"Объединенный список: {result1}")
    
    # б) Функция process_string
    def process_string(text, separator=None):
        if separator:
            words = text.split(separator)
            capitalized = [word.capitalize() for word in words]
            return separator.join(capitalized)
        else:
            return text.lower()
    
    print("\nб) Функция process_string:")
    print("Введите текст:")
    text = input("Текст: ")
    
    print("Введите разделитель (если нужен, иначе Enter):")
    sep = input("Разделитель: ").strip()
    
    if sep:
        result2 = process_string(text, sep)
    else:
        result2 = process_string(text)
    
    print(f"Результат: '{result2}'")
    
    # в) Функция difference
    def difference(first_list, *other_lists):
        result = []
        for item in first_list:
            in_all_others = True
            for other_list in other_lists:
                if item not in other_list:
                    in_all_others = False
                    break
            if not in_all_others:
                result.append(item)
        return result
    
    print("\nв) Функция difference:")
    print("Введите первый список через пробел:")
    first_list = input().split()
    
    print("Сколько дополнительных списков?")
    num_lists = int(input())
    other_lists = []
    
    for i in range(num_lists):
        print(f"Введите список {i+1} через пробел:")
        current_list = input().split()
        other_lists.append(current_list)
    
    result3 = difference(first_list, *other_lists)
    print(f"Элементы только в первом списке: {result3}")
    
    # г) Функция common_in_at_least_two
    def common_in_at_least_two(*lists):
        element_count = {}
        for lst in lists:
            for item in set(lst):
                element_count[item] = element_count.get(item, 0) + 1
        
        return [item for item, count in element_count.items() if count >= 2]
    
    print("\nг) Функция common_in_at_least_two:")
    print("Сколько списков вы хотите ввести?")
    num_lists = int(input())
    lists = []
    
    for i in range(num_lists):
        print(f"Введите список {i+1} через пробел:")
        current_list = input().split()
        lists.append(current_list)
    
    result4 = common_in_at_least_two(*lists)
    print(f"Элементы, встречающиеся хотя бы в двух списках: {result4}")
    
    return result1, result2, result3, result4

def task13():
    print("\n=== ЗАДАНИЕ 13 ===")
    
    # а) Функция divisible_by
    def divisible_by(numbers, divisor=2):
        return [n for n in numbers if n % divisor == 0]
    
    print("а) Функция divisible_by:")
    print("Введите список чисел через пробел:")
    numbers = list(map(int, input().split()))
    
    print("Введите делитель (по умолчанию 2):")
    divisor_input = input().strip()
    if divisor_input:
        divisor = int(divisor_input)
    else:
        divisor = 2
    
    result1 = divisible_by(numbers, divisor)
    print(f"Числа, делящиеся на {divisor}: {result1}")
    
    # б) Функция transform_numbers
    def transform_numbers(numbers, transform_function=None):
        if transform_function:
            return [transform_function(n) for n in numbers]
        else:
            return [n for n in numbers if n >= 0]
    
    print("\nб) Функция transform_numbers:")
    print("Введите список чисел через пробел:")
    numbers = list(map(int, input().split()))
    
    print("Применить преобразование? (y/n):")
    choice = input().lower()
    if choice == 'y':
        print("Введите преобразование (например: x**2, x*10):")
        transform_str = input()
        try:
            transform_func = eval(f"lambda x: {transform_str}")
            result2 = transform_numbers(numbers, transform_func)
        except:
            print("Ошибка в преобразовании, удаляем отрицательные числа")
            result2 = transform_numbers(numbers)
    else:
        result2 = transform_numbers(numbers)
    
    print(f"Результат: {result2}")
    
    # в) Функция sorted_values_by_keys
    def sorted_values_by_keys(*dicts):
        all_items = {}
        for d in dicts:
            all_items.update(d)
        
        sorted_keys = sorted(all_items.keys(), key=lambda k: int(k))
        return [all_items[key] for key in sorted_keys]
    
    print("\nв) Функция sorted_values_by_keys:")
    print("Сколько словарей вы хотите ввести?")
    num_dicts = int(input())
    dicts = []
    
    for i in range(num_dicts):
        print(f"Введите словарь {i+1} в формате 'ключ:значение,ключ:значение' (ключи - числа):")
        dict_str = input()
        pairs = dict_str.split(',')
        current_dict = {}
        for pair in pairs:
            key, value = pair.split(':')
            current_dict[key.strip()] = value.strip()
        dicts.append(current_dict)
    
    result3 = sorted_values_by_keys(*dicts)
    print(f"Значения, отсортированные по ключам: {result3}")
    
    # г) Функция common_keys_in_dicts
    def common_keys_in_dicts(*dicts):
        if not dicts:
            return {}
        
        common_keys = set(dicts[0].keys())
        for d in dicts[1:]:
            common_keys = common_keys.intersection(set(d.keys()))
        
        result = {}
        for key in common_keys:
            # Берем значение из последнего словаря
            for d in reversed(dicts):
                if key in d:
                    result[key] = d[key]
                    break
        
        return result
    
    print("\nг) Функция common_keys_in_dicts:")
    print("Сколько словарей вы хотите ввести?")
    num_dicts = int(input())
    dicts = []
    
    for i in range(num_dicts):
        print(f"Введите словарь {i+1} в формате 'ключ:значение,ключ:значение':")
        dict_str = input()
        pairs = dict_str.split(',')
        current_dict = {}
        for pair in pairs:
            key, value = pair.split(':')
            current_dict[key.strip()] = value.strip()
        dicts.append(current_dict)
    
    result4 = common_keys_in_dicts(*dicts)
    print(f"Ключи, присутствующие во всех словарях: {result4}")
    
    return result1, result2, result3, result4

def task14():
    print("\n=== ЗАДАНИЕ 14 ===")
    
    # а) Функция merge_lists_with
    def merge_lists_with(list1, list2, merge_function=None):
        if merge_function:
            result = []
            min_len = min(len(list1), len(list2))
            for i in range(min_len):
                result.append(merge_function(list1[i], list2[i]))
            return result
        else:
            return list1 + list2
    
    print("а) Функция merge_lists_with:")
    print("Введите первый список чисел через пробел:")
    list1 = list(map(int, input().split()))
    print("Введите второй список чисел через пробел:")
    list2 = list(map(int, input().split()))
    
    print("Использовать функцию объединения? (y/n):")
    choice = input().lower()
    if choice == 'y':
        print("Введите функцию объединения (например: x+y, x*y, max(x,y)):")
        merge_str = input()
        try:
            merge_func = eval(f"lambda x, y: {merge_str}")
            result1 = merge_lists_with(list1, list2, merge_func)
        except:
            print("Ошибка в функции, просто объединяем списки")
            result1 = merge_lists_with(list1, list2)
    else:
        result1 = merge_lists_with(list1, list2)
    
    print(f"Результат: {result1}")
    
    # б) Функция extract_digits
    def extract_digits(strings, digits_only=False):
        if digits_only:
            result = []
            for s in strings:
                digits = ''.join(char for char in s if char.isdigit())
                result.append(digits)
            return result
        else:
            return strings.copy()
    
    print("\nб) Функция extract_digits:")
    print("Введите строки через запятую:")
    strings = [s.strip() for s in input().split(',')]
    
    print("Извлекать только цифры? (y/n):")
    digits_choice = input().lower()
    digits_only = digits_choice == 'y'
    
    result2 = extract_digits(strings, digits_only)
    print(f"Результат: {result2}")
    
    # в) Функция filter_even_numbers
    def filter_even_numbers(*args):
        return [n for n in args if n % 2 == 0]
    
    print("\nв) Функция filter_even_numbers:")
    print("Введите числа через пробел:")
    numbers = list(map(int, input().split()))
    result3 = filter_even_numbers(*numbers)
    print(f"Четные числа: {result3}")
    
    # г) Функция sorted_positive_numbers
    def sorted_positive_numbers(*args):
        positive = [n for n in args if n > 0]
        return sorted(positive, reverse=True)
    
    print("\nг) Функция sorted_positive_numbers:")
    print("Введите числа через пробел:")
    numbers = list(map(int, input().split()))
    result4 = sorted_positive_numbers(*numbers)
    print(f"Положительные числа по убыванию: {result4}")
    
    return result1, result2, result3, result4

def task15():
    print("\n=== ЗАДАНИЕ 15 ===")
    
    # а) Функция change_case
    def change_case(strings, to_upper=False):
        result = ' '.join(strings)
        if to_upper:
            return result.upper()
        else:
            return result.lower()
    
    print("а) Функция change_case:")
    print("Введите строки через запятую:")
    strings = [s.strip() for s in input().split(',')]
    
    print("Преобразовать в верхний регистр? (y/n):")
    upper_choice = input().lower()
    to_upper = upper_choice == 'y'
    
    result1 = change_case(strings, to_upper)
    print(f"Результат: '{result1}'")
    
    # б) Функция filter_combined_lists
    def filter_combined_lists(list1, list2, filter_function=None):
        combined = list1 + list2
        if filter_function:
            return [item for item in combined if filter_function(item)]
        else:
            return combined
    
    print("\nб) Функция filter_combined_lists:")
    print("Введите первый список чисел через пробел:")
    list1 = list(map(int, input().split()))
    print("Введите второй список чисел через пробел:")
    list2 = list(map(int, input().split()))
    
    print("Применить фильтр? (y/n):")
    choice = input().lower()
    if choice == 'y':
        print("Введите условие фильтра (например: x>5, x%2==0):")
        filter_str = input()
        try:
            filter_func = eval(f"lambda x: {filter_str}")
            result2 = filter_combined_lists(list1, list2, filter_func)
        except:
            print("Ошибка в условии, возвращаем объединенный список")
            result2 = filter_combined_lists(list1, list2)
    else:
        result2 = filter_combined_lists(list1, list2)
    
    print(f"Результат: {result2}")
    
    # в) Функция unique_sorted_numbers
    def unique_sorted_numbers(numbers):
        unique = list(set(numbers))
        return sorted(unique)
    
    print("\nв) Функция unique_sorted_numbers:")
    print("Введите числа через пробел:")
    numbers = list(map(int, input().split()))
    result3 = unique_sorted_numbers(numbers)
    print(f"Уникальные отсортированные числа: {result3}")
    
    # г) Функция strings_starting_with_upper
    def strings_starting_with_upper(*args):
        return [s for s in args if s and s[0].isupper()]
    
    print("\nг) Функция strings_starting_with_upper:")
    print("Введите строки через пробел:")
    strings = input().split()
    result4 = strings_starting_with_upper(*strings)
    print(f"Строки, начинающиеся с заглавной буквы: {result4}")
    
    return result1, result2, result3, result4

# Главная программа
def main():
    print("Выберите задание (1-15):")
    choice = input()
    
    if choice == '1':
        result = task1()
    elif choice == '2':
        result = task2()
    elif choice == '3':
        result = task3()
    elif choice == '4':
        result = task4()
    elif choice == '5':
        result = task5()
    elif choice == '6':
        result = task6()
    elif choice == '7':
        result = task7()
    elif choice == '8':
        result = task8()
    elif choice == '9':
        result = task9()
    elif choice == '10':
        result = task10()
    elif choice == '11':
        result = task11()
    elif choice == '12':
        result = task12()
    elif choice == '13':
        result = task13()
    elif choice == '14':
        result = task14()
    elif choice == '15':
        result = task15()
    else:
        print("Неверный выбор!")
        return
    
    print("\nРезультат:", result)

if __name__ == "__main__":
    main()