# ЗАДАНИЕ 12. КОРТЕЖИ (15 задач)

def task12_1():
    print("\n=== ЗАДАНИЕ 12.1 ===")
    # Кортеж из строк -> словарь {строка: длина_заглавных_букв}
    text = input("Введите строки через запятую: ")
    words = text.split(',')
    my_tuple = tuple(words)
    
    result_dict = {}
    for word in my_tuple:
        word = word.strip()
        count = 0
        for letter in word:
            if letter.isupper():
                count += 1
        result_dict[word] = count
    
    print("Кортеж:", my_tuple)
    print("Словарь:", result_dict)
    return my_tuple, result_dict

def task12_2():
    print("\n=== ЗАДАНИЕ 12.2 ===")
    # Разные типы данных -> сортировка по типам
    mixed_tuple = ("hello", 123, 45.6, [1, 2], {"a": 1}, (7, 8))
    print("Смешанный кортеж:", mixed_tuple)
    
    tuple_list = [("text", 1), (2.5, "word"), ([1], 3)]
    
    strings = []
    numbers = []
    lists = []
    dicts = []
    tuples = []
    
    for tup in tuple_list:
        for item in tup:
            if type(item) == str:
                strings.append(item)
            elif type(item) == int or type(item) == float:
                numbers.append(item)
            elif type(item) == list:
                lists.append(item)
            elif type(item) == dict:
                dicts.append(item)
            elif type(item) == tuple:
                tuples.append(item)
    
    print("Строки:", strings)
    print("Числа:", numbers)
    print("Списки:", lists)
    return mixed_tuple, strings

def task12_3():
    print("\n=== ЗАДАНИЕ 12.3 ===")
    # Кортеж чисел -> перевернуть и удалить кратные 3
    text = input("Введите числа через пробел: ")
    numbers = [int(x) for x in text.split()]
    my_tuple = tuple(numbers)
    
    print("Кортеж:", my_tuple)
    print("Первый элемент:", my_tuple[0])
    
    reversed_list = list(my_tuple)
    reversed_list.reverse()
    
    filtered = []
    for num in reversed_list:
        if num % 3 != 0:
            filtered.append(num)
    
    result = tuple(filtered)
    print("Результат:", result)
    return my_tuple, result

def task12_4():
    print("\n=== ЗАДАНИЕ 12.4 ===")
    # Распаковка кортежа -> словарь
    person = ("Иван", 25, "Москва", "инженер")
    name, age, city, job = person
    
    print(f"Имя: {name}, Возраст: {age}, Город: {city}, Работа: {job}")
    
    pairs = [("яблоко", 50), ("банан", 30), ("апельсин", 40)]
    my_dict = dict(pairs)
    
    sorted_items = sorted(my_dict.items(), key=lambda x: x[1])
    sorted_dict = dict(sorted_items)
    
    print("Отсортированный словарь:", sorted_dict)
    return person, sorted_dict

def task12_5():
    print("\n=== ЗАДАНИЕ 12.5 ===")
    # Добавить элемент -> обратные строки
    old_tuple = (1, 2, 3, 4)
    print("Исходный кортеж:", old_tuple)
    
    new_element = input("Введите новый элемент: ")
    new_tuple = old_tuple + (new_element,)
    print("Новый кортеж:", new_tuple)
    
    reversed_strings = []
    for item in new_tuple:
        reversed_str = str(item)[::-1]
        reversed_strings.append(reversed_str)
    
    result = tuple(reversed_strings)
    print("С обратными строками:", result)
    return new_tuple, result

def task12_6():
    print("\n=== ЗАДАНИЕ 12.6 ===")
    # Кортеж в строку -> замена последнего элемента
    my_tuple = ("яблоко", "банан", "апельсин")
    separator = input("Введите разделитель: ")
    result_string = separator.join(my_tuple)
    print("Строка:", result_string)
    
    tuple_list = [(1, 2, 3), (4, 5, 6), (7, 8, "текст")]
    new_value = input("Введите новое значение: ")
    
    new_list = []
    for tup in tuple_list:
        temp_list = list(tup)
        if isinstance(temp_list[-1], (int, float)):
            temp_list[-1] = new_value
        new_list.append(tuple(temp_list))
    
    print("Обновленные кортежи:", new_list)
    return result_string, new_list

def task12_7():
    print("\n=== ЗАДАНИЕ 12.7 ===")
    # Четвертый элемент -> замена пустых кортежей
    my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
    
    if len(my_tuple) >= 4:
        print("4-й с начала:", my_tuple[3])
        print("4-й с конца:", my_tuple[-4])
    
    tuple_list = [(1, 2), (), (3, 4), (), (5, 6)]
    print("Исходный список:", tuple_list)
    
    import random
    new_list = []
    for tup in tuple_list:
        if len(tup) == 0:
            new_list.append((random.randint(1, 10), random.randint(1, 10)))
        else:
            new_list.append(tup)
    
    print("После замены:", new_list)
    return my_tuple, new_list

def task12_8():
    print("\n=== ЗАДАНИЕ 12.8 ===")
    # Кортеж словарей -> сортировка по float
    dict1 = {"name": "Анна", "score": 85.5}
    dict2 = {"name": "Борис", "score": 92.3}
    dict3 = {"name": "Виктор", "score": 78.9}
    
    dict_tuple = (dict1, dict2, dict3)
    print("Кортеж словарей:", dict_tuple)
    
    sorted_list = sorted(dict_tuple, key=lambda x: x["score"], reverse=True)
    sorted_tuple = tuple(sorted_list)
    
    print("После сортировки:", sorted_tuple)
    return dict_tuple, sorted_tuple

def task12_9():
    print("\n=== ЗАДАНИЕ 12.9 ===")
    # Повторяющиеся элементы -> подсчет до кортежа
    my_tuple = (1, 2, 3, 2, 4, 5, 3, 6, 3)
    
    duplicates = []
    for i in range(len(my_tuple)):
        for j in range(i + 1, len(my_tuple)):
            if my_tuple[i] == my_tuple[j] and my_tuple[i] not in duplicates:
                duplicates.append(my_tuple[i])
    
    print("Повторяющиеся элементы:", duplicates)
    
    mixed_list = [1, 2, "hello", 3.14, (4, 5), 6, 7]
    count = 0
    total = 0
    
    for item in mixed_list:
        if type(item) == tuple:
            break
        count += 1
        if isinstance(item, (int, float)):
            total += item
    
    print(f"Элементов до кортежа: {count}, Сумма: {total}")
    return duplicates, total

def task12_10():
    print("\n=== ЗАДАНИЕ 12.10 ===")
    # Поиск элемента -> удаление повторов
    my_tuple = (1, 2, 3, 4, 2, 5, 2, 6)
    
    element = input("Введите элемент для поиска: ")
    try:
        element = int(element)
    except:
        pass
    
    count = my_tuple.count(element)
    print(f"Элемент '{element}' встречается {count} раз")
    
    text = input("Введите строки через запятую: ")
    strings = [s.strip() for s in text.split(',')]
    unique_strings = []
    
    for s in strings:
        if s not in unique_strings:
            unique_strings.append(s)
    
    result = tuple(unique_strings)
    print("Без повторов:", result)
    return count, result

def task12_11():
    print("\n=== ЗАДАНИЕ 12.11 ===")
    # Список в кортеж -> перемножение четных
    text = input("Введите элементы через пробел: ")
    my_list = text.split()
    my_tuple = tuple(my_list)
    print("Кортеж:", my_tuple)
    
    numbers = (2, 3, 4, 5, 6, 7, 8)
    product = 1
    has_even = False
    
    for num in numbers:
        if num % 2 == 0:
            product *= num
            has_even = True
    
    if has_even:
        print("Произведение четных:", product)
    else:
        print("Четных чисел нет")
    return my_tuple, product

def task12_12():
    print("\n=== ЗАДАНИЕ 12.12 ===")
    # Удаление элемента -> среднее в кортежах
    my_tuple = (10, 20, 30, 40, 50)
    print("Исходный кортеж:", my_tuple)
    
    element = input("Введите элемент для удаления: ")
    try:
        element = int(element)
    except:
        pass
    
    new_list = [x for x in my_tuple if x != element]
    new_tuple = tuple(new_list)
    print("После удаления:", new_tuple)
    
    tuple_of_tuples = ((1, 6, 7), (2, 8, 3), (9, 4, 10))
    averages = []
    
    for tup in tuple_of_tuples:
        nums = [x for x in tup if isinstance(x, (int, float)) and x > 5]
        if nums:
            averages.append(sum(nums) / len(nums))
        else:
            averages.append(0)
    
    print("Средние значения:", averages)
    return new_tuple, averages

def task12_13():
    print("\n=== ЗАДАНИЕ 12.13 ===")
    # Срез кортежа -> строки в числа
    my_tuple = (1, "hello", 2, "world", 3, 4, "test")
    print("Исходный кортеж:", my_tuple)
    
    start = int(input("Начало среза: "))
    end = int(input("Конец среза: "))
    
    slice_part = my_tuple[start:end]
    numbers_only = [x for x in slice_part if not isinstance(x, str)]
    print("Срез без строк:", numbers_only)
    
    str_tuple = ("12", "-5", "8", "-3", "15")
    numbers = []
    
    for s in str_tuple:
        num = int(s)
        if num >= 0:
            numbers.append(num)
    
    result = tuple(numbers)
    print("Без отрицательных:", result)
    return numbers_only, result

def task12_14():
    print("\n=== ЗАДАНИЕ 12.14 ===")
    # Поиск номера -> объединение чисел
    my_tuple = (10, "text", 20, 30, "hello", 40)
    
    element = input("Введите элемент для поиска: ")
    try:
        element = int(element)
    except:
        pass
    
    found_index = -1
    for i, item in enumerate(my_tuple):
        if isinstance(item, (int, float)) and item == element:
            found_index = i
            break
    
    if found_index != -1:
        print(f"Найден на позиции {found_index + 1}")
    else:
        print("Не найден")
    
    numbers = (3, 6, 9, 12, 15, 2, 4)
    big_num_str = ''.join(str(x) for x in numbers if x % 3 == 0)
    
    if big_num_str:
        result = int(big_num_str)
        print("Объединенное число:", result)
    else:
        print("Нет чисел кратных 3")
    return found_index, big_num_str

def task12_15():
    print("\n=== ЗАДАНИЕ 12.15 ===")
    # Длина строк -> поиск в кортеже кортежей
    my_tuple = ("apple", 123, "banana", 45.6, "cherry")
    string_count = sum(1 for x in my_tuple if isinstance(x, str))
    print(f"Строковых элементов: {string_count}")
    
    tuple_of_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7))
    element = input("Введите элемент для поиска: ")
    try:
        element = int(element)
    except:
        pass
    
    count = 0
    for tup in tuple_of_tuples:
        count += tup.count(element)
    
    print(f"Элемент встречается {count} раз")
    return string_count, count

# ЗАДАНИЕ 13. МНОЖЕСТВА (15 задач)

def task13_1():
    print("\n=== ЗАДАНИЕ 13.1 ===")
    # а) Создать множества символов
    print("Введите последовательность символов:")
    sequence = input()
    
    digits = set()
    operators = set()
    letters_AF = set()
    letters_XYZ = set()
    
    for char in sequence:
        if char.isdigit():
            digits.add(char)
        elif char in '+-*/':
            operators.add(char)
        elif char.upper() in 'ABCDEF':
            letters_AF.add(char)
        elif char.upper() in 'XYZ':
            letters_XYZ.add(char)
    
    print("Цифры:", digits)
    print("Операторы:", operators)
    print("Буквы A-F:", letters_AF)
    print("Буквы X-Z:", letters_XYZ)
    
    # б) Отсутствующие товары
    print("Введите коды доступных товаров через пробел (1-20):")
    available_input = input().split()
    available = set(int(x) for x in available_input)
    
    all_products = set(range(1, 21))
    missing = all_products - available
    
    print("Отсутствующие товары:", missing)
    return digits, missing

def task13_2():
    print("\n=== ЗАДАНИЕ 13.2 ===")
    # а) Подсчет цифр и операторов
    print("Введите текст:")
    text = input()
    
    digit_count = sum(1 for char in text if char.isdigit())
    operator_count = sum(1 for char in text if char in '+-*/')
    
    print(f"Цифр: {digit_count}, Операторов: {operator_count}")
    
    # б) Общие элементы двух списков
    print("Введите первый список чисел через пробел:")
    list1 = [int(x) for x in input().split()]
    
    print("Введите второй список чисел через пробел:")
    list2 = [int(x) for x in input().split()]
    
    common = set(list1) & set(list2)
    print("Общие элементы:", common)
    return digit_count, common

def task13_3():
    print("\n=== ЗАДАНИЕ 13.3 ===")
    # а) Латинские буквы и знаки препинания
    print("Введите текст на английском:")
    text = input()
    
    lowercase = set(char for char in text if char.islower() and char.isalpha())
    punctuation_count = sum(1 for char in text if char in '.,!?;:')
    
    print("Строчные латинские буквы:", lowercase)
    print("Знаков препинания:", punctuation_count)
    
    # б) Проверка подмножества
    print("Введите элементы множества A через пробел:")
    A = set(input().split())
    
    print("Введите элементы множества B через пробел:")
    B = set(input().split())
    
    is_subset = A.issubset(B)
    print(f"A является подмножеством B: {is_subset}")
    return lowercase, is_subset

def task13_4():
    print("\n=== ЗАДАНИЕ 13.4 ===")
    # а) Общие буквы трех предложений
    print("Введите первое предложение:")
    s1 = input()
    print("Введите второе предложение:")
    s2 = input()
    print("Введите третье предложение:")
    s3 = input()
    
    letters1 = set(char.lower() for char in s1 if char.isalpha())
    letters2 = set(char.lower() for char in s2 if char.isalpha())
    letters3 = set(char.lower() for char in s3 if char.isalpha())
    
    common = letters1 & letters2 & letters3
    print("Общие буквы:", common)
    
    # б) Предметы только одного университета
    print("Введите предметы первого университета через запятую:")
    uni1 = set(x.strip() for x in input().split(','))
    
    print("Введите предметы второго университета через запятую:")
    uni2 = set(x.strip() for x in input().split(','))
    
    only_uni1 = uni1 - uni2
    only_uni2 = uni2 - uni1
    
    print("Только в первом университете:", only_uni1)
    print("Только во втором университете:", only_uni2)
    return common, only_uni1

def task13_5():
    print("\n=== ЗАДАНИЕ 13.5 ===")
    # а) Наибольшая цифра трех чисел
    print("Введите первое число:")
    num1 = int(input())
    print("Введите второе число:")
    num2 = int(input())
    print("Введите третье число:")
    num3 = int(input())
    
    all_digits = set()
    for num in [num1, num2, num3]:
        all_digits.update(str(num))
    
    max_digit = max(int(d) for d in all_digits)
    print("Наибольшая цифра:", max_digit)
    
    # б) Элементы только в одном множестве
    print("Введите элементы множества A через пробел:")
    A = set(input().split())
    
    print("Введите элементы множества B через пробел:")
    B = set(input().split())
    
    only_A = A - B
    only_B = B - A
    unique = only_A | only_B
    
    print("Элементы только в одном множестве:", unique)
    return max_digit, unique

def task13_6():
    print("\n=== ЗАДАНИЕ 13.6 ===")
    # а) Уникальные цифры в строке
    print("Введите строку с цифрами:")
    text = input()
    
    unique_digits = set(char for char in text if char.isdigit())
    print(f"Количество уникальных цифр: {len(unique_digits)}")
    print("Уникальные цифры:", sorted(unique_digits))
    
    # б) Товары одного пользователя
    purchases = [
        {"user": 1, "products": ["laptop", "mouse"]},
        {"user": 2, "products": ["monitor", "mouse"]},
        {"user": 3, "products": ["laptop", "headphones"]}
    ]
    
    product_users = {}
    for purchase in purchases:
        for product in purchase["products"]:
            if product not in product_users:
                product_users[product] = set()
            product_users[product].add(purchase["user"])
    
    unique_products = [p for p, users in product_users.items() if len(users) == 1]
    print("Товары одного пользователя:", unique_products)
    return unique_digits, unique_products

def task13_7():
    print("\n=== ЗАДАНИЕ 13.7 ===")
    # а) Уникальные буквы для трех предложений
    print("Введите первое предложение:")
    s1 = input()
    print("Введите второе предложение:")
    s2 = input()
    print("Введите третье предложение:")
    s3 = input()
    
    def get_letters(text):
        return set(char.lower() for char in text if char.isalpha())
    
    l1, l2, l3 = get_letters(s1), get_letters(s2), get_letters(s3)
    
    unique1 = l1 - l2 - l3
    unique2 = l2 - l1 - l3
    unique3 = l3 - l1 - l2
    
    print("Уникальные для первого:", unique1)
    print("Уникальные для второго:", unique2)
    print("Уникальные для третьего:", unique3)
    
    # б) Непересекающиеся множества
    print("Введите элементы множества A через пробел:")
    A = set(input().split())
    
    print("Введите элементы множества B через пробел:")
    B = set(input().split())
    
    are_disjoint = A.isdisjoint(B)
    print(f"Множества непересекаются: {are_disjoint}")
    return unique1, are_disjoint

def task13_8():
    print("\n=== ЗАДАНИЕ 13.8 ===")
    # а) Составление строки из символов
    print("Введите первую строку:")
    str1 = input()
    print("Введите вторую строку:")
    str2 = input()
    print("Введите целевую строку:")
    target = input()
    
    available = set(str1 + str2)
    can_form = set(target).issubset(available)
    
    print(f"Можно составить '{target}': {can_form}")
    
    # б) Уникальные навыки сотрудников
    employees = [
        {"id": 1, "skills": ["Python", "SQL"]},
        {"id": 2, "skills": ["Python", "JavaScript"]},
        {"id": 3, "skills": ["Java", "SQL"]}
    ]
    
    skill_count = {}
    for emp in employees:
        for skill in emp["skills"]:
            skill_count[skill] = skill_count.get(skill, 0) + 1
    
    unique_skills = [s for s, count in skill_count.items() if count == 1]
    print("Навыки только у одного сотрудника:", unique_skills)
    return can_form, unique_skills

def task13_9():
    print("\n=== ЗАДАНИЕ 13.9 ===")
    # а) Русские гласные буквы
    print("Введите текст на русском:")
    text = input().lower()
    
    vowels = "аеёиоуыэюя"
    found_vowels = set(char for char in text if char in vowels)
    sorted_vowels = sorted(found_vowels)
    
    print("Уникальные русские гласные:", sorted_vowels)
    
    # б) Категории с одним продуктом
    products = [
        {"id": 1, "categories": ["электроника", "телефоны"]},
        {"id": 2, "categories": ["электроника", "компьютеры"]},
        {"id": 3, "categories": ["книги"]}
    ]
    
    category_count = {}
    for product in products:
        for category in product["categories"]:
            category_count[category] = category_count.get(category, 0) + 1
    
    single_categories = [c for c, count in category_count.items() if count == 1]
    print("Категории с одним продуктом:", single_categories)
    return sorted_vowels, single_categories

def task13_10():
    print("\n=== ЗАДАНИЕ 13.10 ===")
    # а) Уникальные цифры числа
    print("Введите число:")
    number = input()
    
    unique_digits = set(char for char in number if char.isdigit())
    sorted_digits = sorted(int(d) for d in unique_digits)
    print("Уникальные цифры:", sorted_digits)
    
    # б) Строгое подмножество
    print("Введите элементы множества A через пробел:")
    A = set(input().split())
    
    print("Введите элементы множества B через пробел:")
    B = set(input().split())
    
    is_strict_subset = A.issubset(B) and A != B
    print(f"A строгое подмножество B: {is_strict_subset}")
    return sorted_digits, is_strict_subset

def task13_11():
    print("\n=== ЗАДАНИЕ 13.11 ===")
    # а) Гласные vs согласные
    print("Введите текст на русском:")
    text = input().lower()
    
    vowels = "аеёиоуыэюя"
    consonants = "бвгджзйклмнпрстфхцчшщ"
    
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char in consonants)
    
    print(f"Гласных: {vowel_count}, Согласных: {consonant_count}")
    
    if vowel_count > consonant_count:
        print("Гласных больше")
    elif consonant_count > vowel_count:
        print("Согласных больше")
    else:
        print("Поровну")
    
    # б) Товары только в определенный день
    orders = [
        {"day": "2024-01-01", "products": ["laptop", "mouse"]},
        {"day": "2024-01-01", "products": ["keyboard", "mouse"]},
        {"day": "2024-01-02", "products": ["laptop", "monitor"]}
    ]
    
    print("Введите день (например: 2024-01-01):")
    target_day = input()
    
    day_products = set()
    other_products = set()
    
    for order in orders:
        if order["day"] == target_day:
            day_products.update(order["products"])
        else:
            other_products.update(order["products"])
    
    only_target = day_products - other_products
    print(f"Товары только за {target_day}: {only_target}")
    return vowel_count, only_target

def task13_12():
    print("\n=== ЗАДАНИЕ 13.12 ===")
    # а) Отсутствующие цифры в числе
    print("Введите натуральное число:")
    number = input()
    
    all_digits = set("0123456789")
    number_digits = set(number)
    missing = sorted(all_digits - number_digits)
    
    print("Отсутствующие цифры:", missing)
    
    # б) Надмножество
    print("Введите элементы множества A через пробел:")
    A = set(input().split())
    
    print("Введите элементы множества B через пробел:")
    B = set(input().split())
    
    is_superset = A.issuperset(B)
    print(f"A надмножество B: {is_superset}")
    return missing, is_superset

def task13_13():
    print("\n=== ЗАДАНИЕ 13.13 ===")
    # а) Удаление пересечения
    print("Введите элементы множества A через пробел:")
    A = set(input().split())
    
    print("Введите элементы множества B через пробел:")
    B = set(input().split())
    
    result = A - B
    print(f"A после удаления пересечения с B: {result}")
    
    # б) Товары купленные хотя бы одним
    purchases = [
        {"user": 1, "products": ["laptop", "mouse"]},
        {"user": 2, "products": ["monitor", "keyboard"]},
        {"user": 3, "products": ["laptop", "headphones"]}
    ]
    
    all_products = set()
    for purchase in purchases:
        all_products.update(purchase["products"])
    
    print("Все купленные товары:", all_products)
    return result, all_products

def task13_14():
    print("\n=== ЗАДАНИЕ 13.14 ===")
    # а) Отсутствующие согласные
    print("Введите текст на русском:")
    text = input().lower()
    
    all_consonants = set("бвгджзйклмнпрстфхцчшщ")
    text_consonants = set(char for char in text if char in all_consonants)
    missing = sorted(all_consonants - text_consonants)
    
    print("Отсутствующие согласные:", missing)
    
    # б) Равные множества
    print("Введите элементы множества A через пробел:")
    A = set(input().split())
    
    print("Введите элементы множества B через пробел:")
    B = set(input().split())
    
    are_equal = A == B
    print(f"Множества равны: {are_equal}")
    return missing, are_equal

def task13_15():
    print("\n=== ЗАДАНИЕ 13.15 ===")
    # а) Общие элементы
    print("Введите элементы множества A через пробел:")
    A = set(input().split())
    
    print("Введите элементы множества B через пробел:")
    B = set(input().split())
    
    has_common = not A.isdisjoint(B)
    common_elements = A & B
    
    print(f"Есть общие элементы: {has_common}")
    print("Общие элементы:", common_elements)
    
    # б) Общие предметы университетов
    print("Введите предметы первого университета через запятую:")
    uni1 = set(x.strip() for x in input().split(','))
    
    print("Введите предметы второго университета через запятую:")
    uni2 = set(x.strip() for x in input().split(','))
    
    common_subjects = uni1 & uni2
    print("Предметы изучаемые в обоих университетах:", common_subjects)
    return has_common, common_subjects

# Главная программа
def main():
    print("Выберите задание (13.1-13.15):")
    choice = input()
    
    if choice == '13.1':
        result = task13_1()
    elif choice == '13.2':
        result = task13_2()
    elif choice == '13.3':
        result = task13_3()
    elif choice == '13.4':
        result = task13_4()
    elif choice == '13.5':
        result = task13_5()
    elif choice == '13.6':
        result = task13_6()
    elif choice == '13.7':
        result = task13_7()
    elif choice == '13.8':
        result = task13_8()
    elif choice == '13.9':
        result = task13_9()
    elif choice == '13.10':
        result = task13_10()
    elif choice == '13.11':
        result = task13_11()
    elif choice == '13.12':
        result = task13_12()
    elif choice == '13.13':
        result = task13_13()
    elif choice == '13.14':
        result = task13_14()
    elif choice == '13.15':
        result = task13_15()
    else:
        print("Неверный выбор!")
        return
    
    print("\nРезультат:", result)

if __name__ == "__main__":
    main()