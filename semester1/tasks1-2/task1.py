# ЗАДАНИЕ 1. Ввод/вывод информации. Оператор =

import math

def task1_1():
    print("\n=== ЗАДАНИЕ 1.1 ===")
    x = float(input("Введите x: "))
    y = 3 * x**2 + math.sin(x + 2)
    print(f"y = {y}")
    return y

def task1_2():
    print("\n=== ЗАДАНИЕ 1.2 ===")
    a = float(input("Введите a: "))
    x = float(input("Введите x: "))
    y = a * x**2 + math.cos(2*x + 1)
    print(f"y = {y}")
    return y

def task1_3():
    print("\n=== ЗАДАНИЕ 1.3 ===")
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    x = float(input("Введите x: "))
    y = a * x + b * math.sin(2*x + 2)
    print(f"y = {y}")
    return y

def task1_4():
    print("\n=== ЗАДАНИЕ 1.4 ===")
    a = float(input("Введите a: "))
    x = float(input("Введите x: "))
    y = a * x**3 + math.cos(3*x + 1)
    print(f"y = {y}")
    return y

def task1_5():
    print("\n=== ЗАДАНИЕ 1.5 ===")
    a = float(input("Введите a: "))
    x = float(input("Введите x: "))
    y = (x**2 / a) + math.cos(2*x - 1)
    print(f"y = {y}")
    return y

def task1_6():
    print("\n=== ЗАДАНИЕ 1.6 ===")
    a = float(input("Введите a: "))
    x = float(input("Введите x: "))
    y = (x / a) + 2 * x**2
    print(f"y = {y}")
    return y

def task1_7():
    print("\n=== ЗАДАНИЕ 1.7 ===")
    x = float(input("Введите x: "))
    y = 3 * x**2 - 2 * x + 1
    print(f"y = {y}")
    return y

def task1_8():
    print("\n=== ЗАДАНИЕ 1.8 ===")
    x = float(input("Введите x: "))
    y = 0.5 * x**2 - 3 * x + 1
    print(f"y = {y}")
    return y

def task1_9():
    print("\n=== ЗАДАНИЕ 1.9 ===")
    a = float(input("Введите a: "))
    x = float(input("Введите x: "))
    y = 1 / (x**2 + 1) - a
    print(f"y = {y}")
    return y

def task1_10():
    print("\n=== ЗАДАНИЕ 1.10 ===")
    a = float(input("Введите a: "))
    x = float(input("Введите x: "))
    y = (a / (x**2 + 1)) - math.cos(2*x - 1)
    print(f"y = {y}")
    return y

def task1_11():
    print("\n=== ЗАДАНИЕ 1.11 ===")
    x = float(input("Введите x: "))
    y = x**3 - 2 * x**2 + 4
    print(f"y = {y}")
    return y

def task1_12():
    print("\n=== ЗАДАНИЕ 1.12 ===")
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    x = float(input("Введите x: "))
    y = a * x**2 + b * x**3 - 8
    print(f"y = {y}")
    return y

def task1_13():
    print("\n=== ЗАДАНИЕ 1.13 ===")
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    x = float(input("Введите x: "))
    y = a * math.sqrt(x**2 + 4) - b
    print(f"y = {y}")
    return y

def task1_14():
    print("\n=== ЗАДАНИЕ 1.14 ===")
    x = float(input("Введите x: "))
    y = math.cos(2*x - 1) + math.sin(x)
    print(f"y = {y}")
    return y

def task1_15():
    print("\n=== ЗАДАНИЕ 1.15 ===")
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    x = float(input("Введите x: "))
    y = a * math.sqrt(x + b * x**2)
    print(f"y = {y}")
    return y

# Главная программа
def main():
    print("Выберите задание (1.1-1.15):")
    choice = input()
    
    if choice == '1.1':
        result = task1_1()
    elif choice == '1.2':
        result = task1_2()
    elif choice == '1.3':
        result = task1_3()
    elif choice == '1.4':
        result = task1_4()
    elif choice == '1.5':
        result = task1_5()
    elif choice == '1.6':
        result = task1_6()
    elif choice == '1.7':
        result = task1_7()
    elif choice == '1.8':
        result = task1_8()
    elif choice == '1.9':
        result = task1_9()
    elif choice == '1.10':
        result = task1_10()
    elif choice == '1.11':
        result = task1_11()
    elif choice == '1.12':
        result = task1_12()
    elif choice == '1.13':
        result = task1_13()
    elif choice == '1.14':
        result = task1_14()
    elif choice == '1.15':
        result = task1_15()
    else:
        print("Неверный выбор!")
        return
    
    print("\nРезультат:", result)

if __name__ == "__main__":
    main()