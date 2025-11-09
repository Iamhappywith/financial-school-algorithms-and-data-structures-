# ЗАДАНИЕ 10. СТРОКИ (15 задач)

def task10_1():
    print("\n=== ЗАДАНИЕ 10.1 ===")
    s = input("Введите строку: ")
    
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    print("Частоты символов:")
    for char, count in char_count.items():
        print(f"'{char}': {count}")
    return char_count

def task10_2():
    print("\n=== ЗАДАНИЕ 10.2 ===")
    s = input("Введите строку: ")
    
    if len(s) < 2:
        print("Длина строки меньше двух символов")
        return ""
    else:
        result = s[:2] + s[-2:]
        print("Результат:", result)
        return result

def task10_3():
    print("\n=== ЗАДАНИЕ 10.3 ===")
    s = input("Введите строку: ")
    
    if len(s) > 0:
        first_char = s[0]
        result = first_char + s[1:].replace(first_char, '$')
        print("Результат:", result)
        return result
    else:
        return ""

def task10_4():
    print("\n=== ЗАДАНИЕ 10.4 ===")
    s1 = input("Введите первую строку: ")
    s2 = input("Введите вторую строку: ")
    
    if len(s1) >= 2 and len(s2) >= 2:
        new_s1 = s2[:2] + s1[2:]
        new_s2 = s1[:2] + s2[2:]
        result = new_s1 + " " + new_s2
        print("Результат:", result)
        return result
    else:
        print("Обе строки должны содержать минимум 2 символа")
        return ""

def task10_5():
    print("\n=== ЗАДАНИЕ 10.5 ===")
    s = input("Введите строку: ")
    
    if len(s) < 3:
        result = s
    elif s.endswith('ing'):
        result = s + 'ly'
    else:
        result = s + 'ing'
    
    print("Результат:", result)
    return result

def task10_6():
    print("\n=== ЗАДАНИЕ 10.6 ===")
    s = input("Введите строку: ")
    n = int(input("Введите n: "))
    
    result = ""
    for i in range(len(s)):
        if (i + 1) % n != 0:
            result += s[i]
    
    print("Результат:", result)
    return result

def task10_7():
    print("\n=== ЗАДАНИЕ 10.7 ===")
    s = input("Введите строку: ")
    
    if len(s) > 0:
        result = s[-1] + s[1:-1] + s[0]
        print("Результат:", result)
        return result
    else:
        return ""

def task10_8():
    print("\n=== ЗАДАНИЕ 10.8 ===")
    s = input("Введите строку: ")
    
    result = s[::2]  # символы с четными индексами
    print("Результат:", result)
    return result

def task10_9():
    print("\n=== ЗАДАНИЕ 10.9 ===")
    s = input("Введите предложение: ")
    
    words = s.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    print("Вхождения слов:")
    for word, count in word_count.items():
        print(f"'{word}': {count}")
    return word_count

def task10_10():
    print("\n=== ЗАДАНИЕ 10.10 ===")
    s = input("Введите строку: ")
    
    if len(s) % 4 == 0:
        result = s[::-1]
        print("Результат:", result)
        return result
    else:
        print("Длина строки не кратна 4")
        return s

def task10_11():
    print("\n=== ЗАДАНИЕ 10.11 ===")
    s = input("Введите строку: ")
    
    if len(s) >= 4:
        upper_count = sum(1 for char in s[:4] if char.isupper())
        if upper_count >= 2:
            result = s.upper()
            print("Результат:", result)
            return result
    
    print("Строка не изменена:", s)
    return s

def task10_12():
    print("\n=== ЗАДАНИЕ 10.12 ===")
    s = input("Введите предложение: ")
    
    result = ""
    for char in s:
        if char.isalpha():
            if char.islower():
                if char == 'z':
                    result += 'a'
                elif char == 'я':
                    result += 'а'
                else:
                    result += chr(ord(char) + 1)
            else:
                if char == 'Z':
                    result += 'A'
                elif char == 'Я':
                    result += 'А'
                else:
                    result += chr(ord(char) + 1)
        else:
            result += char
    
    print("Зашифрованная строка:", result)
    return result

def task10_13():
    print("\n=== ЗАДАНИЕ 10.13 ===")
    s = input("Введите строку: ")
    
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s:
        if char_count[char] == 1:
            print(f"Первый неповторяющийся символ: '{char}'")
            return char
    
    print("Нет неповторяющихся символов")
    return ""

def task10_14():
    print("\n=== ЗАДАНИЕ 10.14 ===")
    s = input("Введите строку: ")
    
    words = s.split()
    result_words = []
    
    for word in words:
        if len(word) > 0:
            if len(word) == 1:
                new_word = word.upper()
            else:
                new_word = word[0].upper() + word[1:-1] + word[-1].upper()
            result_words.append(new_word)
    
    result = ' '.join(result_words)
    print("Результат:", result)
    return result

def task10_15():
    print("\n=== ЗАДАНИЕ 10.15 ===")
    s = input("Введите строку (цифры и латинские буквы): ")
    
    # Извлекаем только буквы
    letters = [char for char in s if char.isalpha()]
    
    # Проверяем, упорядочены ли буквы по алфавиту
    is_sorted = True
    violation_index = -1
    
    for i in range(1, len(letters)):
        if letters[i] < letters[i-1]:
            is_sorted = False
            # Находим индекс в исходной строке
            for j, char in enumerate(s):
                if char == letters[i]:
                    violation_index = j
                    break
            break
    
    if is_sorted:
        print("0")
        return 0
    else:
        print(f"Нарушение порядка на позиции: {violation_index + 1}")
        return violation_index + 1

# Главная программа
def main():
    print("Выберите задание (10.1-10.15):")
    choice = input()
    
    if choice == '10.1':
        result = task10_1()
    elif choice == '10.2':
        result = task10_2()
    elif choice == '10.3':
        result = task10_3()
    elif choice == '10.4':
        result = task10_4()
    elif choice == '10.5':
        result = task10_5()
    elif choice == '10.6':
        result = task10_6()
    elif choice == '10.7':
        result = task10_7()
    elif choice == '10.8':
        result = task10_8()
    elif choice == '10.9':
        result = task10_9()
    elif choice == '10.10':
        result = task10_10()
    elif choice == '10.11':
        result = task10_11()
    elif choice == '10.12':
        result = task10_12()
    elif choice == '10.13':
        result = task10_13()
    elif choice == '10.14':
        result = task10_14()
    elif choice == '10.15':
        result = task10_15()
    else:
        print("Неверный выбор!")
        return
    
    print("\nРезультат:", result)

if __name__ == "__main__":
    main()