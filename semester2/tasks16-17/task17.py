# ЗАДАНИЕ 1-15. РЕКУРСИВНЫЕ ФУНКЦИИ (15 задач)

def task1():
    print("\n=== ЗАДАНИЕ 1 ===")
    
    # а) Функция Fact - факториал
    def Fact(N):
        if N == 0 or N == 1:
            return 1
        return N * Fact(N - 1)
    
    # б) Функция Fact2 - двойной факториал
    def Fact2(N):
        if N == 1 or N == 2:
            return N
        return N * Fact2(N - 2)
    
    print("а) Функция Fact - вычисление факториала")
    print("Введите число N (N > 0):")
    n = int(input("N = "))
    if n > 0:
        result1 = Fact(n)
        print(f"{n}! = {result1}")
    else:
        print("N должно быть больше 0")
        result1 = None
    
    print("\nб) Функция Fact2 - вычисление двойного факториала")
    print("Введите число N (N > 0):")
    n = int(input("N = "))
    if n > 0:
        result2 = Fact2(n)
        print(f"{n}!! = {result2}")
    else:
        print("N должно быть больше 0")
        result2 = None
    
    return result1, result2

def task2():
    print("\n=== ЗАДАНИЕ 2 ===")
    
    def PowerN(x, n):
        if n == 0:
            return 1
        elif n > 0:
            return x * PowerN(x, n - 1)
        else:
            return 1 / PowerN(x, -n)
    
    print("Функция PowerN - вычисление степени числа")
    print("Введите число x (x ≥ 0):")
    x = float(input("x = "))
    print("Введите степень n (целое число):")
    n = int(input("n = "))
    
    if x >= 0:
        result = PowerN(x, n)
        print(f"{x}^{n} = {result}")
    else:
        print("x должно быть неотрицательным")
        result = None
    
    return result

def task3():
    print("\n=== ЗАДАНИЕ 3 ===")
    
    def SqrtK(x, k, n):
        if n == 0:
            return 1
        else:
            y_prev = SqrtK(x, k, n - 1)
            return y_prev - (y_prev - x / (y_prev ** (k - 1))) / k
    
    print("Функция SqrtK - приближенное значение корня k-й степени")
    print("Введите число x (x > 0):")
    x = float(input("x = "))
    print("Введите степень корня k (k > 1):")
    k = int(input("k = "))
    print("Введите количество итераций n (n > 0):")
    n = int(input("n = "))
    
    if x > 0 and k > 1 and n > 0:
        result = SqrtK(x, k, n)
        print(f"Корень {k}-й степени из {x} (при n={n}) = {result}")
        print(f"Проверка: {result}^{k} = {result ** k}")
    else:
        print("Условия: x > 0, k > 1, n > 0")
        result = None
    
    return result

def task4():
    print("\n=== ЗАДАНИЕ 4 ===")
    
    call_count = 0
    
    def FibRec(N):
        nonlocal call_count
        call_count += 1
        
        if N == 1 or N == 2:
            return 1
        return FibRec(N - 2) + FibRec(N - 1)
    
    print("Функция FibRec - числа Фибоначчи")
    print("Введите 5 номеров чисел Фибоначчи через пробел:")
    numbers = list(map(int, input().split()))
    
    results = []
    total_calls = 0
    
    for num in numbers:
        call_count = 0
        fib_num = FibRec(num)
        results.append((num, fib_num, call_count))
        total_calls += call_count
    
    print("\nРезультаты:")
    for num, fib_num, calls in results:
        print(f"F({num}) = {fib_num}, рекурсивных вызовов: {calls}")
    
    print(f"Всего рекурсивных вызовов: {total_calls}")
    
    return results

def task5():
    print("\n=== ЗАДАНИЕ 5 ===")
    
    call_count = 0
    
    def C(m, n):
        nonlocal call_count
        call_count += 1
        
        if m == 0 or m == n:
            return 1
        return C(m, n - 1) + C(m - 1, n - 1)
    
    print("Функция C - число сочетаний")
    print("Введите число N (n > 0):")
    N = int(input("N = "))
    print("Введите 5 различных значений M через пробел (0 ≤ M ≤ N):")
    M_values = list(map(int, input().split()))
    
    results = []
    total_calls = 0
    
    for M in M_values:
        if 0 <= M <= N:
            call_count = 0
            comb = C(M, N)
            results.append((M, N, comb, call_count))
            total_calls += call_count
    
    print("\nРезультаты:")
    for m, n, comb, calls in results:
        print(f"C({m}, {n}) = {comb}, рекурсивных вызовов: {calls}")
    
    print(f"Всего рекурсивных вызовов: {total_calls}")
    
    return results

def task6():
    print("\n=== ЗАДАНИЕ 6 ===")
    
    def MOD(A, B):
        if A == 0:
            return B
        return MOD(B % A, A)
    
    print("Функция MOD - наибольший общий делитель (алгоритм Евклида)")
    print("Введите число A:")
    A = int(input("A = "))
    print("Введите число B:")
    B = int(input("B = "))
    print("Введите число C:")
    C = int(input("C = "))
    print("Введите число D:")
    D = int(input("D = "))
    
    result1 = MOD(A, B)
    result2 = MOD(A, C)
    result3 = MOD(A, D)
    
    print(f"НОД({A}, {B}) = {result1}")
    print(f"НОД({A}, {C}) = {result2}")
    print(f"НОД({A}, {D}) = {result3}")
    
    return result1, result2, result3

def task7():
    print("\n=== ЗАДАНИЕ 7 ===")
    
    def MinRec(A, N):
        if N == 1:
            return A[0]
        min_rest = MinRec(A, N - 1)
        return A[N - 1] if A[N - 1] < min_rest else min_rest
    
    print("Функция MinRec - минимальный элемент массива")
    
    arrays = []
    for i in range(3):
        print(f"Введите массив {i+1} через пробел:")
        arr = list(map(int, input().split()))
        arrays.append(arr)
    
    results = []
    for i, arr in enumerate(arrays):
        if arr:
            min_val = MinRec(arr, len(arr))
            results.append((f"Массив {i+1}", min_val))
    
    print("\nРезультаты:")
    for arr_name, min_val in results:
        print(f"{arr_name}: минимальный элемент = {min_val}")
    
    return results

def task8():
    print("\n=== ЗАДАНИЕ 8 ===")
    
    def Digits(S):
        if not S:
            return 0
        first_char = S[0]
        rest = S[1:]
        if first_char.isdigit():
            return 1 + Digits(rest)
        else:
            return Digits(rest)
    
    print("Функция Digits - количество цифр в строке")
    print("Введите строку:")
    S = input("S = ")
    
    result = Digits(S)
    print(f"Количество цифр в строке: {result}")
    
    return result

def task9():
    print("\n=== ЗАДАНИЕ 9 ===")
    
    def Simm(S):
        if len(S) <= 1:
            return True
        if S[0] != S[-1]:
            return False
        return Simm(S[1:-1])
    
    print("Функция Simm - проверка симметричности строки")
    print("Введите строку для проверки:")
    S = input("S = ")
    
    result = Simm(S)
    print(f"Строка '{S}' симметрична: {result}")
    
    return result

def task10():
    print("\n=== ЗАДАНИЕ 10 ===")
    
    def binary_to_decimal(binary_str):
        if not binary_str:
            return 0
        if binary_str[0] == '-':
            return -binary_to_decimal(binary_str[1:])
        
        return int(binary_str, 2)
    
    def decimal_to_binary(n):
        if n == 0:
            return "0"
        if n < 0:
            return "-" + decimal_to_binary(-n)
        
        def to_bin_pos(x):
            if x == 0:
                return ""
            return to_bin_pos(x // 2) + str(x % 2)
        
        result = to_bin_pos(abs(n))
        return result if result else "0"
    
    def binary_addition(a, b):
        # Преобразуем в десятичные числа для сложения
        dec_a = binary_to_decimal(a)
        dec_b = binary_to_decimal(b)
        result_dec = dec_a + dec_b
        
        # Преобразуем результат обратно в двоичную систему
        return decimal_to_binary(result_dec)
    
    print("Сложение чисел в двоичной системе")
    print("Введите положительное число в двоичной системе:")
    pos_binary = input("Положительное число: ")
    print("Введите отрицательное число в двоичной системе:")
    neg_binary = input("Отрицательное число: ")
    
    result = binary_addition(pos_binary, neg_binary)
    
    print(f"\n{pos_binary}₂ + ({neg_binary}₂) = {result}₂")
    
    # Проверка
    dec1 = binary_to_decimal(pos_binary)
    dec2 = binary_to_decimal(neg_binary)
    print(f"Проверка: {dec1} + ({dec2}) = {dec1 + dec2}")
    
    return result

def task11():
    print("\n=== ЗАДАНИЕ 11 ===")
    
    def f(x):
        # Пример функции: x^2 - 2 = 0 (корень √2 ≈ 1.414)
        return x**2 - 2
    
    def Root(a, b, epsilon, func):
        mid = (a + b) / 2
        if abs(b - a) < epsilon or abs(func(mid)) < epsilon:
            return mid
        
        if func(a) * func(mid) < 0:
            return Root(a, mid, epsilon, func)
        else:
            return Root(mid, b, epsilon, func)
    
    print("Функция Root - нахождение корня методом деления отрезка пополам")
    print("Уравнение: x² - 2 = 0")
    print("Введите левую границу a:")
    a = float(input("a = "))
    print("Введите правую границу b:")
    b = float(input("b = "))
    print("Введите точность ε:")
    epsilon = float(input("ε = "))
    
    if a < b and f(a) * f(b) < 0:
        result = Root(a, b, epsilon, f)
        print(f"Корень уравнения: {result:.6f}")
        print(f"Проверка: f({result:.6f}) = {f(result):.6f}")
    else:
        print("Условия не выполнены: a < b и f(a)*f(b) < 0")
        result = None
    
    return result

def task12():
    print("\n=== ЗАДАНИЕ 12 ===")
    
    def reverse_number(n, reversed_so_far=0):
        if n == 0:
            return reversed_so_far
        last_digit = n % 10
        remaining = n // 10
        return reverse_number(remaining, reversed_so_far * 10 + last_digit)
    
    print("Функция reverse_number - переворот числа")
    print("Введите число n (десятичная запись не содержит нулей):")
    n = int(input("n = "))
    
    # Проверка на нули в числе
    if '0' in str(n):
        print("Ошибка: число не должно содержать нулей")
        return None
    
    result = reverse_number(n)
    print(f"Число {n} в обратном порядке: {result}")
    
    return result

def task13():
    print("\n=== ЗАДАНИЕ 13 ===")
    
    def Simm_part(S, i, j):
        if i >= j:
            return True
        if S[i] != S[j]:
            return False
        return Simm_part(S, i + 1, j - 1)
    
    print("Функция Simm_part - проверка симметричности части строки")
    print("Введите строку:")
    S = input("S = ")
    print("Введите начальный индекс i:")
    i = int(input("i = "))
    print("Введите конечный индекс j:")
    j = int(input("j = "))
    
    if 0 <= i <= j < len(S):
        result = Simm_part(S, i, j)
        substring = S[i:j+1]
        print(f"Подстрока '{substring}' симметрична: {result}")
    else:
        print("Неверные индексы")
        result = None
    
    return result

def task14():
    print("\n=== ЗАДАНИЕ 14 ===")
    
    def sum_of_digits(N):
        if N == 0:
            return 0
        return (N % 10) + sum_of_digits(N // 10)
    
    print("Функция sum_of_digits - сумма цифр числа")
    print("Введите натуральное число N:")
    N = int(input("N = "))
    
    if N > 0:
        result = sum_of_digits(N)
        print(f"Сумма цифр числа {N}: {result}")
    else:
        print("N должно быть натуральным числом")
        result = None
    
    return result

def task15():
    print("\n=== ЗАДАНИЕ 15 ===")
    
    def is_palindrome(word):
        if len(word) <= 1:
            return True
        if word[0] != word[-1]:
            return False
        return is_palindrome(word[1:-1])
    
    print("Функция is_palindrome - проверка палиндрома")
    print("Введите слово (только строчные латинские буквы):")
    word = input("Слово: ")
    
    # Проверка на строчные латинские буквы
    if word.isalpha() and word.islower():
        result = is_palindrome(word)
        print(f"Слово '{word}' является палиндромом: {'yes' if result else 'no'}")
    else:
        print("Слово должно содержать только строчные латинские буквы")
        result = None
    
    return result

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