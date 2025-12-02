# РАБОТА С ФАЙЛАМИ

import os

# === ЗАДАЧА 1 ===
def task1():
    print("=== Задача 1 ===")
    print("Создать новый файл с K последними строками")
    
    # Создаем тестовый файл
    with open('file1.txt', 'w') as f:
        f.write("Строка 1\n")
        f.write("Строка 2\n")
        f.write("Строка 3\n")
        f.write("Строка 4\n")
        f.write("Строка 5\n")
    
    print("Исходный файл создан")
    
    # Читаем файл
    with open('file1.txt', 'r') as f:
        lines = f.readlines()  # читаем все строки в список
    
    print(f"Всего строк: {len(lines)}")
    
    # Выбираем K последних строк
    K = 3
    last_lines = lines[-K:]  # берем последние K строк
    
    # Записываем в новый файл
    with open('last_lines.txt', 'w') as f:
        for line in last_lines:
            f.write(line)
    
    print(f"Создан новый файл с {K} последними строками")
    
    # Показываем результат
    print("\nНовый файл содержит:")
    with open('last_lines.txt', 'r') as f:
        print(f.read())
    
    # Удаляем временные файлы
    os.remove('file1.txt')
    os.remove('last_lines.txt')

# === ЗАДАЧА 2 ===
def task2():
    print("\n=== Задача 2 ===")
    print("Удалить из файла последние K строк")
    
    # Создаем тестовый файл
    with open('file2.txt', 'w') as f:
        for i in range(1, 11):
            f.write(f"Строка {i}\n")
    
    print("Исходный файл создан (10 строк)")
    
    # Читаем файл
    with open('file2.txt', 'r') as f:
        lines = f.readlines()
    
    K = 4
    # Оставляем все строки кроме последних K
    new_lines = lines[:-K]
    
    # Записываем обратно в файл
    with open('file2.txt', 'w') as f:
        for line in new_lines:
            f.write(line)
    
    print(f"Удалены последние {K} строк")
    print(f"Осталось строк: {len(new_lines)}")
    
    # Удаляем временный файл
    os.remove('file2.txt')

# === ЗАДАЧА 3 ===
def task3():
    print("\n=== Задача 3 ===")
    print("Удалить из каждой строки первые K символов")
    
    # Создаем тестовый файл
    with open('file3.txt', 'w') as f:
        f.write("12345Привет\n")
        f.write("67Мир\n")
        f.write("Программирование\n")
    
    print("Исходный файл создан")
    
    # Читаем файл
    with open('file3.txt', 'r') as f:
        lines = f.readlines()
    
    K = 2
    new_lines = []
    
    # Обрабатываем каждую строку
    for line in lines:
        # Если строка короче K символов, оставляем пустую строку
        if len(line) > K:
            new_line = line[K:]  # берем все символы начиная с K
            new_lines.append(new_line)
        else:
            new_lines.append('\n')  # пустая строка
    
    # Записываем в файл
    with open('new_file3.txt', 'w') as f:
        for line in new_lines:
            f.write(line)
    
    print("Новый файл создан")
    print(f"Из каждой строки удалено {K} символов")
    
    # Удаляем временные файлы
    os.remove('file3.txt')
    os.remove('new_file3.txt')

# === ЗАДАЧА 4 ===
def task4():
    print("\n=== Задача 4 ===")
    print("Добавить к строкам первого файла строки второго файла")
    
    # Создаем первый файл
    with open('file4a.txt', 'w') as f:
        f.write("Строка A1\n")
        f.write("Строка A2\n")
        f.write("Строка A3\n")
        f.write("Строка A4\n")
    
    # Создаем второй файл
    with open('file4b.txt', 'w') as f:
        f.write("+Дополнение1\n")
        f.write("+Дополнение2\n")
        f.write("+Дополнение3\n")
    
    print("Два файла созданы")
    
    # Читаем оба файла
    with open('file4a.txt', 'r') as f:
        lines1 = f.readlines()
    
    with open('file4b.txt', 'r') as f:
        lines2 = f.readlines()
    
    # Объединяем строки
    result = []
    for i in range(len(lines1)):
        line1 = lines1[i].strip()  # убираем \n
        if i < len(lines2):
            line2 = lines2[i].strip()
            result.append(line1 + " " + line2 + "\n")
        else:
            result.append(line1 + "\n")
    
    # Записываем результат
    with open('result4.txt', 'w') as f:
        for line in result:
            f.write(line)
    
    print("Файлы объединены")
    
    # Удаляем временные файлы
    os.remove('file4a.txt')
    os.remove('file4b.txt')
    os.remove('result4.txt')

# === ЗАДАЧА 5 ===
def task5():
    print("\n=== Задача 5 ===")
    print("Удалить строку с номером K")
    
    # Создаем тестовый файл
    with open('file5.txt', 'w') as f:
        for i in range(1, 6):
            f.write(f"Строка номер {i}\n")
    
    print("Файл создан (5 строк)")
    
    # Читаем файл
    with open('file5.txt', 'r') as f:
        lines = f.readlines()
    
    print(f"Всего строк: {len(lines)}")
    
    K = 3  # удаляем 3-ю строку
    if 1 <= K <= len(lines):
        # Создаем новый список без K-й строки
        new_lines = []
        for i in range(len(lines)):
            if i != K-1:  # i начинается с 0, K - с 1
                new_lines.append(lines[i])
        
        # Записываем в файл
        with open('file5.txt', 'w') as f:
            for line in new_lines:
                f.write(line)
        
        print(f"Строка номер {K} удалена")
        print(f"Осталось строк: {len(new_lines)}")
    else:
        print(f"Строки с номером {K} нет в файле")
    
    # Удаляем временный файл
    os.remove('file5.txt')

# === ЗАДАЧА 6 ===
def task6():
    print("\n=== Задача 6 ===")
    print("Создать файл со знаками препинания")
    
    # Создаем тестовый файл с текстом
    with open('text6.txt', 'w') as f:
        f.write("Привет, мир! Как дела?\n")
        f.write("Сегодня - хороший день.\n")
        f.write("Программирование: это интересно!\n")
    
    print("Текстовый файл создан")
    
    # Читаем файл
    with open('text6.txt', 'r') as f:
        text = f.read()
    
    # Собираем знаки препинания
    punctuation = ""
    for char in text:
        # Проверяем, является ли символ знаком препинания
        if char in ",.!?;:-()\"'":
            punctuation += char
    
    # Записываем знаки препинания в новый файл
    with open('punctuation.txt', 'w') as f:
        f.write(punctuation)
    
    print(f"Найдено {len(punctuation)} знаков препинания")
    print(f"Знаки препинания: {punctuation}")
    
    # Удаляем временные файлы
    os.remove('text6.txt')
    os.remove('punctuation.txt')

# === ЗАДАЧА 7 ===
def task7():
    print("\n=== Задача 7 ===")
    print("Посчитать числа в файле")
    
    # Создаем файл с числами и пробелами
    with open('numbers.txt', 'w') as f:
        f.write("   123   \n")
        f.write("  45  \n")
        f.write("   6789   \n")
        f.write("  0  \n")
    
    print("Файл с числами создан")
    
    # Читаем файл
    with open('numbers.txt', 'r') as f:
        lines = f.readlines()
    
    count = 0
    total = 0
    
    for line in lines:
        # Убираем пробелы в начале и конце
        cleaned = line.strip()
        if cleaned:  # если строка не пустая
            number = int(cleaned)  # преобразуем в число
            count += 1
            total += number
            print(f"Найдено число: {number}")
    
    print(f"\nВсего чисел: {count}")
    print(f"Сумма чисел: {total}")
    
    os.remove('numbers.txt')
    return count, total

# === ЗАДАЧА 8 ===
def task8():
    print("\n=== Задача 8 ===")
    print("Заменить пустые строки на строку S")
    
    # Создаем тестовый файл
    with open('text8.txt', 'w') as f:
        f.write("Первая строка\n")
        f.write("\n")  # пустая строка
        f.write("Третья строка\n")
        f.write("\n")  # пустая строка
        f.write("\n")  # пустая строка
        f.write("Последняя строка\n")
    
    print("Файл создан (с пустыми строками)")
    
    # Читаем файл
    with open('text8.txt', 'r') as f:
        lines = f.readlines()
    
    S = "ЗАМЕНА"
    new_lines = []
    
    for line in lines:
        if line.strip() == "":  # если строка пустая (только пробелы или \n)
            new_lines.append(S + "\n")
        else:
            new_lines.append(line)
    
    # Записываем обратно
    with open('text8.txt', 'w') as f:
        for line in new_lines:
            f.write(line)
    
    print(f"Пустые строки заменены на '{S}'")
    
    # Показываем результат
    print("\nРезультат:")
    with open('text8.txt', 'r') as f:
        print(f.read())
    
    os.remove('text8.txt')

# === ЗАДАЧА 9 ===
def task9():
    print("\n=== Задача 9 ===")
    print("Выровнять текст по центру")
    
    # Создаем текст, выровненный по левому краю
    with open('left.txt', 'w') as f:
        f.write("Привет\n")
        f.write("Это текст\n")
        f.write("Программирование\n")
        f.write("Python\n")
    
    print("Файл создан (текст по левому краю)")
    
    # Читаем файл
    with open('left.txt', 'r') as f:
        lines = f.readlines()
    
    width = 50  # ширина текста
    centered_lines = []
    
    for line in lines:
        line = line.strip()  # убираем \n
        if line:  # если строка не пустая
            # Дополняем строку пробелом, если она нечетной длины
            if len(line) % 2 == 1:
                line = " " + line
            
            # Вычисляем сколько пробелов добавить слева
            spaces = (width - len(line)) // 2
            centered_line = " " * spaces + line + "\n"
            centered_lines.append(centered_line)
        else:
            centered_lines.append("\n")  # пустую строку оставляем
    
    # Записываем результат
    with open('centered.txt', 'w') as f:
        for line in centered_lines:
            f.write(line)
    
    print("Текст выровнен по центру (ширина 50)")
    
    # Показываем результат
    print("\nРезультат (добавлены пробелы в начале):")
    with open('centered.txt', 'r') as f:
        for line in centered_lines:
            print(repr(line))  # repr показывает пробелы
    
    os.remove('left.txt')
    os.remove('centered.txt')

# === ЗАДАЧА 10 ===
def task10():
    print("\n=== Задача 10 ===")
    print("Найти количество абзацев")
    
    # Создаем текст с абзацами
    with open('text10.txt', 'w') as f:
        f.write("Первый абзац.\n")
        f.write("Продолжение первого абзаца.\n")
        f.write("\n")  # пустая строка - разделитель абзацев
        f.write("Второй абзац.\n")
        f.write("\n")  # пустая строка
        f.write("\n")  # еще пустая строка
        f.write("Третий абзац.\n")
        f.write("Еще строка третьего абзаца.\n")
    
    print("Текст с абзацами создан")
    
    # Читаем файл
    with open('text10.txt', 'r') as f:
        lines = f.readlines()
    
    paragraph_count = 0
    in_paragraph = False
    
    for line in lines:
        if line.strip():  # если строка не пустая
            if not in_paragraph:
                paragraph_count += 1
                in_paragraph = True
        else:  # если строка пустая
            in_paragraph = False
    
    print(f"Количество абзацев: {paragraph_count}")
    
    os.remove('text10.txt')
    return paragraph_count

# === ЗАДАЧА 11 ===
def task11():
    print("\n=== Задача 11 ===")
    print("Выровнять текст по правому краю")
    
    # Создаем текст
    with open('text11.txt', 'w') as f:
        f.write("Привет\n")
        f.write("Мир\n")
        f.write("Программирование\n")
    
    print("Файл создан")
    
    # Читаем файл
    with open('text11.txt', 'r') as f:
        lines = f.readlines()
    
    width = 50
    right_lines = []
    
    for line in lines:
        line = line.strip()
        if line:
            spaces = width - len(line)
            right_line = " " * spaces + line + "\n"
            right_lines.append(right_line)
        else:
            right_lines.append("\n")
    
    # Записываем результат
    with open('right.txt', 'w') as f:
        for line in right_lines:
            f.write(line)
    
    print("Текст выровнен по правому краю")
    
    os.remove('text11.txt')
    os.remove('right.txt')

# === ЗАДАЧА 12 ===
def task12():
    print("\n=== Задача 12 ===")
    print("Добавить второй файл в начало первого")
    
    # Создаем первый файл
    with open('first12.txt', 'w') as f:
        f.write("Содержимое первого файла\n")
        f.write("Вторая строка первого файла\n")
    
    # Создаем второй файл
    with open('second12.txt', 'w') as f:
        f.write("=== НАЧАЛО ===\n")
        f.write("Добавляемый текст\n")
    
    print("Два файла созданы")
    
    # Читаем оба файла
    with open('first12.txt', 'r') as f:
        first_content = f.read()
    
    with open('second12.txt', 'r') as f:
        second_content = f.read()
    
    # Объединяем: второй файл + первый файл
    combined = second_content + first_content
    
    # Записываем обратно в первый файл
    with open('first12.txt', 'w') as f:
        f.write(combined)
    
    print("Второй файл добавлен в начало первого")
    
    os.remove('first12.txt')
    os.remove('second12.txt')

# === ЗАДАЧА 13 ===
def task13():
    print("\n=== Задача 13 ===")
    print("Вставить пустую строку перед строкой K")
    
    # Создаем файл
    with open('text13.txt', 'w') as f:
        for i in range(1, 6):
            f.write(f"Строка {i}\n")
    
    print("Файл создан (5 строк)")
    
    # Читаем файл
    with open('text13.txt', 'r') as f:
        lines = f.readlines()
    
    K = 3  # вставляем пустую строку перед 3-й строкой
    
    if 1 <= K <= len(lines):
        new_lines = []
        for i in range(len(lines)):
            if i == K-1:  # перед K-й строкой
                new_lines.append("\n")  # пустая строка
            new_lines.append(lines[i])
        
        # Записываем обратно
        with open('text13.txt', 'w') as f:
            for line in new_lines:
                f.write(line)
        
        print(f"Пустая строка вставлена перед строкой {K}")
    else:
        print(f"Строки {K} нет в файле")
    
    os.remove('text13.txt')

# === ЗАДАЧА 14 ===
def task14():
    print("\n=== Задача 14 ===")
    print("Продублировать все пустые строки")
    
    # Создаем файл с пустыми строками
    with open('text14.txt', 'w') as f:
        f.write("Первая строка\n")
        f.write("\n")  # пустая
        f.write("Третья строка\n")
        f.write("\n")  # пустая
        f.write("Пятая строка\n")
    
    print("Файл создан")
    
    # Читаем файл
    with open('text14.txt', 'r') as f:
        lines = f.readlines()
    
    new_lines = []
    
    for line in lines:
        new_lines.append(line)
        if line.strip() == "":  # если строка пустая
            new_lines.append("\n")  # добавляем еще одну пустую
    
    # Записываем обратно
    with open('text14.txt', 'w') as f:
        for line in new_lines:
            f.write(line)
    
    print("Пустые строки продублированы")
    
    os.remove('text14.txt')

# === ЗАДАЧА 15 ===
def task15():
    print("\n=== Задача 15 ===")
    print("Удалить первую и последнюю строки")
    
    # Создаем файл
    with open('text15.txt', 'w') as f:
        f.write("Первая строка (будет удалена)\n")
        f.write("Вторая строка\n")
        f.write("Третья строка\n")
        f.write("Четвертая строка\n")
        f.write("Последняя строка (будет удалена)\n")
    
    print("Файл создан (5 строк)")
    
    # Читаем файл
    with open('text15.txt', 'r') as f:
        lines = f.readlines()
    
    if len(lines) > 2:
        # Удаляем первую строку (индекс 0)
        # Удаляем последнюю строку (последний элемент)
        new_lines = lines[1:-1]  # берем все строки кроме первой и последней
        
        # Записываем обратно
        with open('text15.txt', 'w') as f:
            for line in new_lines:
                f.write(line)
        
        print("Первая и последняя строки удалены")
        print(f"Осталось строк: {len(new_lines)}")
    else:
        print("Файл слишком короткий")
    
    os.remove('text15.txt')

# === ГЛАВНОЕ МЕНЮ ===
def main():
    print("ПРОСТЫЕ ЗАДАЧИ ПО РАБОТЕ С ФАЙЛАМИ")
    print("=" * 40)
    
    while True:
        print("\nВыберите задачу (1-15) или 0 для выхода:")
        choice = input("> ")
        
        if choice == '0':
            print("Выход из программы")
            break
        elif choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            task3()
        elif choice == '4':
            task4()
        elif choice == '5':
            task5()
        elif choice == '6':
            task6()
        elif choice == '7':
            task7()
        elif choice == '8':
            task8()
        elif choice == '9':
            task9()
        elif choice == '10':
            task10()
        elif choice == '11':
            task11()
        elif choice == '12':
            task12()
        elif choice == '13':
            task13()
        elif choice == '14':
            task14()
        elif choice == '15':
            task15()
        else:
            print("Неверный выбор! Введите число от 0 до 15")

# Запуск программы
if __name__ == "__main__":
    main()