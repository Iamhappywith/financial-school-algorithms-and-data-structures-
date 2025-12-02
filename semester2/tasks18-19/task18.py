# ЗАДАНИЯ ПО МОДУЛЯМ (15 задач)

# === МОДУЛЬ 1: Геометрия отрезков и треугольников ===
def module1():
    print("\n=== МОДУЛЬ 1 ===")
    print("Функции для работы с отрезками и треугольниками")
    
    # Вспомогательные функции модуля
    def midpoint(x1, y1, x2, y2):
        """Вычисление середины отрезка"""
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        return mx, my
    
    def can_form_triangle(a, b, c):
        """Проверка возможности построения треугольника"""
        return (a + b > c) and (a + c > b) and (b + c > a)
    
    def triangle_area(a, b, c):
        """Вычисление площади треугольника по формуле Герона"""
        if not can_form_triangle(a, b, c):
            return 0
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area
    
    # Пример использования
    print("\nПример 1: Середина отрезка")
    x1, y1 = 0, 0
    x2, y2 = 4, 6
    mx, my = midpoint(x1, y1, x2, y2)
    print(f"Середина отрезка ({x1},{y1})-({x2},{y2}): ({mx:.1f},{my:.1f})")
    
    print("\nПример 2: Проверка треугольника")
    sides = [3, 4, 5]
    print(f"Можно ли построить треугольник со сторонами {sides}? {can_form_triangle(*sides)}")
    
    print("\nПример 3: Площадь треугольника")
    area = triangle_area(*sides)
    print(f"Площадь треугольника со сторонами {sides}: {area:.2f}")
    
    return mx, my, can_form_triangle(*sides), area

# === МОДУЛЬ 2: Работа с точками на плоскости ===
def module2():
    print("\n=== МОДУЛЬ 2 ===")
    print("Функции для работы с точками на плоскости")
    
    def distance(x1, y1, x2, y2):
        """Расстояние между двумя точками"""
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    def triangle_perimeter(p1, p2, p3):
        """Периметр треугольника по координатам вершин"""
        a = distance(*p1, *p2)
        b = distance(*p2, *p3)
        c = distance(*p3, *p1)
        
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            return 0
        return a + b + c
    
    def triangle_area_points(p1, p2, p3):
        """Площадь треугольника по координатам вершин"""
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        
        area = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
        return area
    
    # Пример использования
    print("\nПример: Три точки на плоскости")
    A = (0, 0)
    B = (4, 0)
    C = (0, 3)
    
    print(f"Точка A{A}, Точка B{B}, Точка C{C}")
    print(f"Расстояние AB: {distance(*A, *B):.2f}")
    print(f"Расстояние BC: {distance(*B, *C):.2f}")
    print(f"Расстояние CA: {distance(*C, *A):.2f}")
    
    perimeter = triangle_perimeter(A, B, C)
    area = triangle_area_points(A, B, C)
    
    print(f"Периметр треугольника: {perimeter:.2f}")
    print(f"Площадь треугольника: {area:.2f}")
    
    return distance(*A, *B), perimeter, area

# === МОДУЛЬ 3: Работа с дробями ===
def module3():
    print("\n=== МОДУЛЬ 3 ===")
    print("Функции для работы с дробями")
    
    def gcd(a, b):
        """Нахождение НОД двух чисел"""
        while b:
            a, b = b, a % b
        return abs(a)
    
    def simplify_fraction(p, q):
        """Приведение дроби к несократимому виду"""
        if q == 0:
            return p, q
        
        d = gcd(p, q)
        return p // d, q // d
    
    def fraction_to_decimal(p, q):
        """Перевод дроби в десятичную форму"""
        if q == 0:
            return float('inf')
        return p / q
    
    # Пример использования
    print("\nПример 1: НОД чисел")
    num1, num2 = 48, 18
    result = gcd(num1, num2)
    print(f"НОД({num1}, {num2}) = {result}")
    
    print("\nПример 2: Сокращение дроби")
    p, q = 24, 36
    simplified = simplify_fraction(p, q)
    print(f"Дробь {p}/{q} в несократимом виде: {simplified[0]}/{simplified[1]}")
    
    print("\nПример 3: Перевод в десятичную форму")
    decimal = fraction_to_decimal(p, q)
    print(f"Дробь {p}/{q} в десятичной форме: {decimal:.3f}")
    
    return result, simplified, decimal

# === МОДУЛЬ 4: Аналитическая геометрия ===
def module4():
    print("\n=== МОДУЛЬ 4 ===")
    print("Функции для работы с прямыми на плоскости")
    
    def line_equation(x1, y1, x2, y2):
        """Построение уравнения прямой через две точки"""
        if x1 == x2:
            return f"x = {x1}"
        
        A = y2 - y1
        B = x1 - x2
        C = x2 * y1 - x1 * y2
        
        # Приводим к виду Ax + By + C = 0
        return A, B, C
    
    def are_parallel(A1, B1, C1, A2, B2, C2):
        """Проверка параллельности прямых"""
        # Прямые параллельны, если A1/B1 = A2/B2
        if B1 == 0 and B2 == 0:
            return True
        if B1 == 0 or B2 == 0:
            return False
        return abs(A1/B1 - A2/B2) < 1e-10
    
    def point_on_line(A, B, C, x, y):
        """Проверка принадлежности точки прямой"""
        return abs(A * x + B * y + C) < 1e-10
    
    # Пример использования
    print("\nПример: Работа с прямыми")
    
    # Первая прямая через точки (0,0) и (1,1)
    eq1 = line_equation(0, 0, 1, 1)
    print(f"Уравнение прямой через (0,0) и (1,1): {eq1}")
    
    # Вторая прямая через точки (0,1) и (1,2)
    eq2 = line_equation(0, 1, 1, 2)
    print(f"Уравнение прямой через (0,1) и (1,2): {eq2}")
    
    # Проверка параллельности
    parallel = are_parallel(*eq1, *eq2)
    print(f"Прямые параллельны? {parallel}")
    
    # Проверка принадлежности точки
    point_check = point_on_line(*eq1, 0.5, 0.5)
    print(f"Точка (0.5,0.5) лежит на первой прямой? {point_check}")
    
    return eq1, eq2, parallel, point_check

# === МОДУЛЬ 5: Геометрия круга ===
def module5():
    print("\n=== МОДУЛЬ 5 ===")
    print("Функции для вычислений с кругом")
    
    import math
    
    def circle_area(r):
        """Площадь круга"""
        return math.pi * r ** 2
    
    def circle_circumference(r):
        """Длина окружности"""
        return 2 * math.pi * r
    
    def sector_area(r, angle_degrees):
        """Площадь сектора круга"""
        return math.pi * r ** 2 * angle_degrees / 360
    
    def inscribed_square_perimeter(r):
        """Периметр квадрата, вписанного в окружность"""
        side = r * math.sqrt(2)
        return 4 * side
    
    # Пример использования
    print("\nПример: Вычисления для круга радиусом 5")
    radius = 5
    
    area = circle_area(radius)
    circumference = circle_circumference(radius)
    sector = sector_area(radius, 90)  # 90 градусов
    square_perimeter = inscribed_square_perimeter(radius)
    
    print(f"Площадь круга: {area:.2f}")
    print(f"Длина окружности: {circumference:.2f}")
    print(f"Площадь сектора (90°): {sector:.2f}")
    print(f"Периметр вписанного квадрата: {square_perimeter:.2f}")
    
    return area, circumference, sector, square_perimeter

# === МОДУЛЬ 6: Работа со строками ===
def module6():
    print("\n=== МОДУЛЬ 6 ===")
    print("Функции для работы со строками")
    
    def remove_char(text, char):
        """Удаление заданного символа из строки"""
        return text.replace(char, '')
    
    def replace_char(text, old_char, new_char):
        """Замена одного символа на другой"""
        return text.replace(old_char, new_char)
    
    def count_char(text, char):
        """Подсчет количества заданного символа в строке"""
        return text.count(char)
    
    # Пример использования
    print("\nПример: Работа со строкой 'Hello, World!'")
    text = "Hello, World!"
    
    removed = remove_char(text, 'o')
    replaced = replace_char(text, 'l', 'L')
    count_o = count_char(text, 'l')
    
    print(f"Исходная строка: {text}")
    print(f"Без символа 'o': {removed}")
    print(f"С заменой 'l' на 'L': {replaced}")
    print(f"Количество символов 'l': {count_o}")
    
    return removed, replaced, count_o

# === МОДУЛЬ 7: Матрицы ===
def module7():
    print("\n=== МОДУЛЬ 7 ===")
    print("Функции для работы с матрицами")
    
    def print_matrix(matrix):
        """Вывод матрицы на экран"""
        for row in matrix:
            print(' '.join(f'{elem:4}' for elem in row))
        print()
    
    def add_matrices(A, B):
        """Сложение матриц"""
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            return None
        
        result = []
        for i in range(len(A)):
            row = []
            for j in range(len(A[0])):
                row.append(A[i][j] + B[i][j])
            result.append(row)
        return result
    
    def multiply_matrices(A, B):
        """Умножение матриц"""
        if len(A[0]) != len(B):
            return None
        
        result = []
        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                sum_val = 0
                for k in range(len(B)):
                    sum_val += A[i][k] * B[k][j]
                row.append(sum_val)
            result.append(row)
        return result
    
    def transpose_matrix(A):
        """Транспонирование матрицы"""
        result = []
        for j in range(len(A[0])):
            row = []
            for i in range(len(A)):
                row.append(A[i][j])
            result.append(row)
        return result
    
    # Пример использования
    print("\nПример: Работа с матрицами 2x2")
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    
    print("Матрица A:")
    print_matrix(A)
    
    print("Матрица B:")
    print_matrix(B)
    
    C = add_matrices(A, B)
    print("Сумма A + B:")
    print_matrix(C)
    
    D = multiply_matrices(A, B)
    print("Произведение A * B:")
    print_matrix(D)
    
    T = transpose_matrix(A)
    print("Транспонированная A:")
    print_matrix(T)
    
    return C, D, T

# === МОДУЛЬ 8: Векторы ===
def module8():
    print("\n=== МОДУЛЬ 8 ===")
    print("Функции для работы с векторами")
    
    def vector_add(v1, v2):
        """Сложение векторов"""
        if len(v1) != len(v2):
            return None
        return [v1[i] + v2[i] for i in range(len(v1))]
    
    def scalar_multiply(v, scalar):
        """Умножение вектора на число"""
        return [x * scalar for x in v]
    
    def vector_min_max(v):
        """Поиск минимального и максимального элементов вектора"""
        return min(v), max(v)
    
    # Пример использования
    print("\nПример: Работа с векторами")
    v1 = [1, 2, 3, 4, 5]
    v2 = [5, 4, 3, 2, 1]
    
    print(f"Вектор v1: {v1}")
    print(f"Вектор v2: {v2}")
    
    sum_vec = vector_add(v1, v2)
    scaled = scalar_multiply(v1, 2)
    v_min, v_max = vector_min_max(v1)
    
    print(f"Сумма векторов: {sum_vec}")
    print(f"v1 * 2: {scaled}")
    print(f"Минимум в v1: {v_min}, Максимум в v1: {v_max}")
    
    return sum_vec, scaled, (v_min, v_max)

# === МОДУЛЬ 9: Работа с файлами ===
def module9():
    print("\n=== МОДУЛЬ 9 ===")
    print("Функции для работы с текстовыми файлами")
    
    import os
    
    def create_test_file():
        """Создание тестового файла"""
        content = """Hello World 123!
This is a test file 456.
Line 3 with numbers 789.
End of file 0."""
        
        with open('test_file.txt', 'w', encoding='utf-8') as f:
            f.write(content)
    
    def remove_digits_from_file(filename):
        """Удаление цифр из файла"""
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Удаляем все цифры
        new_content = ''.join(ch for ch in content if not ch.isdigit())
        
        with open('no_digits_' + filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return new_content
    
    def count_chars_in_file(filename):
        """Подсчет количества символов в файле"""
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return len(content)
    
    def count_lines_in_file(filename):
        """Подсчет количества строк в файле"""
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return len(lines)
    
    # Пример использования
    print("\nПример: Работа с файлом")
    
    # Создаем тестовый файл
    create_test_file()
    filename = 'test_file.txt'
    
    # Удаляем цифры
    print("Создан тестовый файл 'test_file.txt'")
    no_digits_content = remove_digits_from_file(filename)
    print("Создан файл без цифр: 'no_digits_test_file.txt'")
    
    # Подсчитываем характеристики
    char_count = count_chars_in_file(filename)
    line_count = count_lines_in_file(filename)
    
    print(f"Количество символов в исходном файле: {char_count}")
    print(f"Количество строк в исходном файле: {line_count}")
    
    # Чистим за собой
    if os.path.exists('test_file.txt'):
        os.remove('test_file.txt')
    if os.path.exists('no_digits_test_file.txt'):
        os.remove('no_digits_test_file.txt')
    
    return char_count, line_count

# === МОДУЛЬ 10: Комплексные числа ===
def module10():
    print("\n=== МОДУЛЬ 10 ===")
    print("Функции для работы с комплексными числами")
    
    def complex_modulus(z):
        """Модуль комплексного числа"""
        real, imag = z
        return (real ** 2 + imag ** 2) ** 0.5
    
    def complex_multiply(z1, z2):
        """Умножение комплексных чисел"""
        a, b = z1
        c, d = z2
        return (a * c - b * d, a * d + b * c)
    
    def complex_divide(z1, z2):
        """Деление комплексных чисел"""
        a, b = z1
        c, d = z2
        denominator = c ** 2 + d ** 2
        if denominator == 0:
            return (float('inf'), float('inf'))
        return ((a * c + b * d) / denominator, (b * c - a * d) / denominator)
    
    # Пример использования
    print("\nПример: Работа с комплексными числами")
    z1 = (3, 4)  # 3 + 4i
    z2 = (1, 2)  # 1 + 2i
    
    print(f"z1 = {z1[0]} + {z1[1]}i")
    print(f"z2 = {z2[0]} + {z2[1]}i")
    
    mod1 = complex_modulus(z1)
    product = complex_multiply(z1, z2)
    quotient = complex_divide(z1, z2)
    
    print(f"Модуль z1: {mod1:.2f}")
    print(f"Произведение z1 * z2: {product[0]:.1f} + {product[1]:.1f}i")
    print(f"Частное z1 / z2: {quotient[0]:.1f} + {quotient[1]:.1f}i")
    
    return mod1, product, quotient

# === МОДУЛЬ 11: Дополнительные операции с дробями ===
def module11():
    print("\n=== МОДУЛЬ 11 ===")
    print("Дополнительные операции с обыкновенными дробями")
    
    def fraction_power(p, q, n):
        """Возведение дроби в степень"""
        return p ** n, q ** n
    
    def fractions_equal(p1, q1, p2, q2):
        """Проверка равенства дробей"""
        return p1 * q2 == p2 * q1
    
    def fraction_greater(p1, q1, p2, q2):
        """Сравнение дробей: первая > вторая"""
        return p1 * q2 > p2 * q1
    
    def fraction_less(p1, q1, p2, q2):
        """Сравнение дробей: первая < вторая"""
        return p1 * q2 < p2 * q1
    
    # Пример использования
    print("\nПример: Операции с дробями")
    frac1 = (1, 2)  # 1/2
    frac2 = (2, 4)  # 2/4 = 1/2
    frac3 = (2, 3)  # 2/3
    
    print(f"Дробь 1: {frac1[0]}/{frac1[1]}")
    print(f"Дробь 2: {frac2[0]}/{frac2[1]}")
    print(f"Дробь 3: {frac3[0]}/{frac3[1]}")
    
    # Возведение в степень
    powered = fraction_power(*frac1, 3)
    print(f"({frac1[0]}/{frac1[1]})^3 = {powered[0]}/{powered[1]}")
    
    # Сравнения
    equal = fractions_equal(*frac1, *frac2)
    greater = fraction_greater(*frac3, *frac1)
    less = fraction_less(*frac1, *frac3)
    
    print(f"Дробь 1 = Дробь 2? {equal}")
    print(f"Дробь 3 > Дробь 1? {greater}")
    print(f"Дробь 1 < Дробь 3? {less}")
    
    return powered, equal, greater, less

# === МОДУЛЬ 12: Векторы на плоскости ===
def module12():
    print("\n=== МОДУЛЬ 12 ===")
    print("Операции над векторами на плоскости")
    
    def vector_subtract(v1, v2):
        """Вычитание векторов"""
        return (v1[0] - v2[0], v1[1] - v2[1])
    
    def dot_product(v1, v2):
        """Скалярное произведение векторов"""
        return v1[0] * v2[0] + v1[1] * v2[1]
    
    def vector_length(v):
        """Длина вектора"""
        return (v[0] ** 2 + v[1] ** 2) ** 0.5
    
    # Пример использования
    print("\nПример: Операции с векторами")
    v1 = (3, 4)
    v2 = (1, 2)
    
    print(f"Вектор v1 = {v1}")
    print(f"Вектор v2 = {v2}")
    
    subtraction = vector_subtract(v1, v2)
    dot = dot_product(v1, v2)
    length1 = vector_length(v1)
    
    print(f"v1 - v2 = {subtraction}")
    print(f"v1 · v2 (скалярное произведение) = {dot}")
    print(f"Длина вектора v1 = {length1:.2f}")
    
    return subtraction, dot, length1

# === МОДУЛЬ 13: Сортировка массивов ===
def module13():
    print("\n=== МОДУЛЬ 13 ===")
    print("Алгоритмы сортировки одномерных массивов")
    
    def insertion_sort(arr):
        """Сортировка вставками"""
        array = arr.copy()
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array
    
    def bubble_sort(arr):
        """Сортировка обменом (пузырьковая)"""
        array = arr.copy()
        n = len(array)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array
    
    def selection_sort(arr):
        """Сортировка выбором"""
        array = arr.copy()
        n = len(array)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if array[j] < array[min_idx]:
                    min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i]
        return array
    
    # Пример использования
    print("\nПример: Сортировка массива")
    original = [64, 34, 25, 12, 22, 11, 90]
    print(f"Исходный массив: {original}")
    
    sorted_insertion = insertion_sort(original)
    sorted_bubble = bubble_sort(original)
    sorted_selection = selection_sort(original)
    
    print(f"Сортировка вставками: {sorted_insertion}")
    print(f"Сортировка обменом:   {sorted_bubble}")
    print(f"Сортировка выбором:   {sorted_selection}")
    
    return sorted_insertion, sorted_bubble, sorted_selection

# === МОДУЛЬ 14: Матричные операции ===
def module14():
    print("\n=== МОДУЛЬ 14 ===")
    print("Операции с матрицами")
    
    def matrix_min(matrix):
        """Поиск минимального элемента матрицы"""
        min_val = float('inf')
        for row in matrix:
            min_val = min(min_val, min(row))
        return min_val
    
    def matrix_max(matrix):
        """Поиск максимального элемента матрицы"""
        max_val = float('-inf')
        for row in matrix:
            max_val = max(max_val, max(row))
        return max_val
    
    def matrix_sum(matrix):
        """Вычисление суммы всех элементов матрицы"""
        total = 0
        for row in matrix:
            total += sum(row)
        return total
    
    def row_sum(matrix, row_index):
        """Вычисление суммы элементов заданной строки"""
        if 0 <= row_index < len(matrix):
            return sum(matrix[row_index])
        return 0
    
    # Пример использования
    print("\nПример: Работа с матрицей 3x3")
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Матрица:")
    for row in matrix:
        print(row)
    
    min_val = matrix_min(matrix)
    max_val = matrix_max(matrix)
    total_sum = matrix_sum(matrix)
    row_1_sum = row_sum(matrix, 1)
    
    print(f"\nМинимальный элемент: {min_val}")
    print(f"Максимальный элемент: {max_val}")
    print(f"Сумма всех элементов: {total_sum}")
    print(f"Сумма элементов строки 1 (индекс 1): {row_1_sum}")
    
    return min_val, max_val, total_sum, row_1_sum

# === МОДУЛЬ 15: Дроби (сложение, вычитание, умножение) ===
def module15():
    print("\n=== МОДУЛЬ 15 ===")
    print("Арифметические операции с обыкновенными дробями")
    
    def gcd(a, b):
        """Нахождение НОД"""
        while b:
            a, b = b, a % b
        return abs(a)
    
    def simplify_fraction(p, q):
        """Сокращение дроби"""
        if q == 0:
            return p, q
        d = gcd(p, q)
        return p // d, q // d
    
    def add_fractions(p1, q1, p2, q2):
        """Сложение дробей"""
        numerator = p1 * q2 + p2 * q1
        denominator = q1 * q2
        return simplify_fraction(numerator, denominator)
    
    def subtract_fractions(p1, q1, p2, q2):
        """Вычитание дробей"""
        numerator = p1 * q2 - p2 * q1
        denominator = q1 * q2
        return simplify_fraction(numerator, denominator)
    
    def multiply_fractions(p1, q1, p2, q2):
        """Умножение дробей"""
        numerator = p1 * p2
        denominator = q1 * q2
        return simplify_fraction(numerator, denominator)
    
    # Пример использования
    print("\nПример: Арифметика дробей")
    frac1 = (1, 2)  # 1/2
    frac2 = (1, 3)  # 1/3
    
    print(f"Дробь 1: {frac1[0]}/{frac1[1]}")
    print(f"Дробь 2: {frac2[0]}/{frac2[1]}")
    
    sum_result = add_fractions(*frac1, *frac2)
    diff_result = subtract_fractions(*frac1, *frac2)
    prod_result = multiply_fractions(*frac1, *frac2)
    
    print(f"\n1/2 + 1/3 = {sum_result[0]}/{sum_result[1]}")
    print(f"1/2 - 1/3 = {diff_result[0]}/{diff_result[1]}")
    print(f"1/2 × 1/3 = {prod_result[0]}/{prod_result[1]}")
    
    return sum_result, diff_result, prod_result

# Главная программа
def main():
    print("ВЫБЕРИТЕ МОДУЛЬ (1-15):")
    print("1. Геометрия отрезков и треугольников")
    print("2. Работа с точками на плоскости")
    print("3. Работа с дробями (НОД, сокращение)")
    print("4. Аналитическая геометрия")
    print("5. Геометрия круга")
    print("6. Работа со строками")
    print("7. Матрицы (базовые операции)")
    print("8. Векторы (числовые)")
    print("9. Работа с файлами")
    print("10. Комплексные числа")
    print("11. Дроби (степень, сравнение)")
    print("12. Векторы на плоскости")
    print("13. Сортировка массивов")
    print("14. Матричные операции")
    print("15. Дроби (арифметика)")
    
    choice = input("\nВведите номер модуля (1-15): ")
    
    modules = {
        '1': module1, '2': module2, '3': module3, '4': module4, '5': module5,
        '6': module6, '7': module7, '8': module8, '9': module9, '10': module10,
        '11': module11, '12': module12, '13': module13, '14': module14, '15': module15
    }
    
    if choice in modules:
        result = modules[choice]()
        print(f"\nМодуль {choice} выполнен успешно!")
        return result
    else:
        print("Неверный выбор! Введите число от 1 до 15.")
        return None

if __name__ == "__main__":
    main()