# ЗАДАНИЕ 9. СТРОКИ (15 задач)

def task9_1():
    print("\n=== ЗАДАНИЕ 9.1 ===")
    s = input("Введите строку: ")
    words = s.split()
    count = len(words)
    print(f"Количество слов: {count}")
    return count

def task9_2():
    print("\n=== ЗАДАНИЕ 9.2 ===")
    s = input("Введите строку заглавными буквами: ")
    words = s.split()
    count = 0
    for word in words:
        if word and word[0] == word[-1]:
            count += 1
    print(f"Слов, начинающихся и заканчивающихся одной буквой: {count}")
    return count

def task9_3():
    print("\n=== ЗАДАНИЕ 9.3 ===")
    s = input("Введите строку заглавными буквами: ")
    words = s.split()
    count = 0
    for word in words:
        if 'А' in word:
            count += 1
    print(f"Слов, содержащих букву 'А': {count}")
    return count

def task9_4():
    print("\n=== ЗАДАНИЕ 9.4 ===")
    s = input("Введите строку: ")
    words = s.split()
    if words:
        min_len = min(len(word) for word in words)
        print(f"Длина самого короткого слова: {min_len}")
        return min_len
    else:
        print("Строка пустая")
        return 0

def task9_5():
    print("\n=== ЗАДАНИЕ 9.5 ===")
    s = input("Введите строку: ")
    words = s.split()
    reversed_words = words[::-1]
    result = ' '.join(reversed_words)
    print("Строка в обратном порядке:", result)
    return result

def task9_6():
    print("\n=== ЗАДАНИЕ 9.6 ===")
    s = input("Введите строку заглавными буквами: ")
    words = s.split()
    sorted_words = sorted(words)
    result = ' '.join(sorted_words)
    print("Строка в алфавитном порядке:", result)
    return result

def task9_7():
    print("\n=== ЗАДАНИЕ 9.7 ===")
    C = input("Введите символ C: ")
    S = input("Введите строку S: ")
    S0 = input("Введите строку S0: ")
    
    result = S.replace(C, S0 + C)
    print("Результат:", result)
    return result

def task9_8():
    print("\n=== ЗАДАНИЕ 9.8 ===")
    s = input("Введите строку с избыточными пробелами: ")
    words = s.split()
    result = ' '.join(words)
    print("Строка с одним пробелом:", result)
    return result

def task9_9():
    print("\n=== ЗАДАНИЕ 9.9 ===")
    s = input("Введите строку: ")
    count = 0
    for char in s:
        if char.islower() and (char.isalpha() or 'а' <= char <= 'я'):
            count += 1
    print(f"Количество строчных букв: {count}")
    return count

def task9_10():
    print("\n=== ЗАДАНИЕ 9.10 ===")
    s = input("Введите строку: ")
    words = s.split()
    if words:
        max_len = max(len(word) for word in words)
        print(f"Длина самого длинного слова: {max_len}")
        return max_len
    else:
        print("Строка пустая")
        return 0

def task9_11():
    print("\n=== ЗАДАНИЕ 9.11 ===")
    s = input("Введите строку: ")
    
    even_chars = s[1::2]  # символы на четных позициях
    odd_chars = s[0::2]   # символы на нечетных позициях
    
    result = even_chars + odd_chars[::-1]
    print("Зашифрованная строка:", result)
    return result

def task9_12():
    print("\n=== ЗАДАНИЕ 9.12 ===")
    S = input("Введите строку S: ")
    N = int(input("Введите число N: "))
    
    result = ('*' * N).join(S)
    print("Результат:", result)
    return result

def task9_13():
    print("\n=== ЗАДАНИЕ 9.13 ===")
    s = input("Введите строку: ")
    
    words = s.split()
    result = '*'.join(words)
    print("Результат:", result)
    return result

def task9_14():
    print("\n=== ЗАДАНИЕ 9.14 ===")
    filename = input("Введите полный путь к файлу: ")
    
    # Извлекаем имя файла с расширением
    full_name = filename.split('\\')[-1]
    # Убираем расширение
    name_only = full_name.split('.')[0]
    
    print("Имя файла без расширения:", name_only)
    return name_only

def task9_15():
    print("\n=== ЗАДАНИЕ 9.15 ===")
    s = input("Введите строку: ")
    
    words = s.split()
    if not words:
        print("Строка пустая")
        return ""
    
    # Находим максимальную длину
    max_len = max(len(word) for word in words)
    # Берем последнее слово с максимальной длиной
    result = ""
    for word in words:
        if len(word) == max_len:
            result = word
    
    print("Самое длинное слово (последнее):", result)
    return result

# Главная программа
def main():
    print("Выберите задание (9.1-9.15):")
    choice = input()
    
    if choice == '9.1':
        result = task9_1()
    elif choice == '9.2':
        result = task9_2()
    elif choice == '9.3':
        result = task9_3()
    elif choice == '9.4':
        result = task9_4()
    elif choice == '9.5':
        result = task9_5()
    elif choice == '9.6':
        result = task9_6()
    elif choice == '9.7':
        result = task9_7()
    elif choice == '9.8':
        result = task9_8()
    elif choice == '9.9':
        result = task9_9()
    elif choice == '9.10':
        result = task9_10()
    elif choice == '9.11':
        result = task9_11()
    elif choice == '9.12':
        result = task9_12()
    elif choice == '9.13':
        result = task9_13()
    elif choice == '9.14':
        result = task9_14()
    elif choice == '9.15':
        result = task9_15()
    else:
        print("Неверный выбор!")
        return
    
    print("\nРезультат", result)

if __name__ == "__main__":
    main()