# ЗАДАНИЕ 2. Ввод/вывод информации. Оператор =

import math

def task2_1():
    print("\n=== ЗАДАНИЕ 2.1 ===")
    a = float(input("Введите длину a: "))
    b = float(input("Введите ширину b: "))
    c = float(input("Введите высоту c: "))
    
    V = a * b * c
    S = 2 * (a * b + b * c + a * c)
    
    print(f"Объем V = {V}")
    print(f"Площадь поверхности S = {S}")
    return V, S

def task2_2():
    print("\n=== ЗАДАНИЕ 2.2 ===")
    R = float(input("Введите радиус R: "))
    
    L = 2 * math.pi * R
    S = math.pi * R**2
    
    print(f"Длина окружности L = {L}")
    print(f"Площадь круга S = {S}")
    return L, S

def task2_3():
    print("\n=== ЗАДАНИЕ 2.3 ===")
    a = float(input("Введите катет a: "))
    b = float(input("Введите катет b: "))
    
    c = math.sqrt(a**2 + b**2)
    P = a + b + c
    
    print(f"Гипотенуза c = {c}")
    print(f"Периметр P = {P}")
    return c, P

def task2_4():
    print("\n=== ЗАДАНИЕ 2.4 ===")
    R1 = float(input("Введите внешний радиус R1: "))
    R2 = float(input("Введите внутренний радиус R2: "))
    
    S1 = math.pi * R1**2
    S2 = math.pi * R2**2
    S3 = S1 - S2
    
    print(f"Площадь большого круга S1 = {S1}")
    print(f"Площадь малого круга S2 = {S2}")
    print(f"Площадь кольца S3 = {S3}")
    return S1, S2, S3

def task2_5():
    print("\n=== ЗАДАНИЕ 2.5 ===")
    x1 = float(input("Введите x1: "))
    y1 = float(input("Введите y1: "))
    x2 = float(input("Введите x2: "))
    y2 = float(input("Введите y2: "))
    
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    
    P = 2 * (width + height)
    S = width * height
    
    print(f"Периметр P = {P}")
    print(f"Площадь S = {S}")
    return P, S

def task2_6():
    print("\n=== ЗАДАНИЕ 2.6 ===")
    x1 = float(input("Введите x1: "))
    y1 = float(input("Введите y1: "))
    x2 = float(input("Введите x2: "))
    y2 = float(input("Введите y2: "))
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    print(f"Расстояние между точками = {distance}")
    return distance

def task2_7():
    print("\n=== ЗАДАНИЕ 2.7 ===")
    x1 = float(input("Введите x1: "))
    y1 = float(input("Введите y1: "))
    x2 = float(input("Введите x2: "))
    y2 = float(input("Введите y2: "))
    x3 = float(input("Введите x3: "))
    y3 = float(input("Введите y3: "))
    
    # Вычисляем длины сторон
    a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    
    P = a + b + c
    p = P / 2  # полупериметр
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    print(f"Периметр P = {P}")
    print(f"Площадь S = {S}")
    return P, S

def task2_8():
    print("\n=== ЗАДАНИЕ 2.8 ===")
    T_f = float(input("Введите температуру в градусах Фаренгейта: "))
    
    T_c = (T_f - 32) * 5 / 9
    
    print(f"Температура в градусах Цельсия = {T_c}")
    return T_c

def task2_9():
    print("\n=== ЗАДАНИЕ 2.9 ===")
    X = float(input("Введите вес шоколадных конфет (кг): "))
    A = float(input("Введите стоимость шоколадных конфет (руб): "))
    Y = float(input("Введите вес ирисок (кг): "))
    B = float(input("Введите стоимость ирисок (руб): "))
    
    price_chocolate = A / X
    price_toffee = B / Y
    ratio = price_chocolate / price_toffee
    
    print(f"Цена 1 кг шоколадных конфет = {price_chocolate}")
    print(f"Цена 1 кг ирисок = {price_toffee}")
    print(f"Шоколадные конфеты дороже ирисок в {ratio} раз")
    return price_chocolate, price_toffee, ratio

def task2_10():
    print("\n=== ЗАДАНИЕ 2.10 ===")
    A1 = float(input("Введите A1: "))
    B1 = float(input("Введите B1: "))
    C1 = float(input("Введите C1: "))
    A2 = float(input("Введите A2: "))
    B2 = float(input("Введите B2: "))
    C2 = float(input("Введите C2: "))
    
    D = A1 * B2 - A2 * B1
    
    if D == 0:
        print("Система не имеет единственного решения")
        return None
    
    x = (C1 * B2 - C2 * B1) / D
    y = (A1 * C2 - A2 * C1) / D
    
    print(f"x = {x}")
    print(f"y = {y}")
    return x, y

def task2_11():
    print("\n=== ЗАДАНИЕ 2.11 ===")
    alpha_deg = float(input("Введите угол в градусах (0-360): "))
    
    alpha_rad = alpha_deg * math.pi / 180
    
    print(f"Угол в радианах = {alpha_rad}")
    return alpha_rad

def task2_12():
    print("\n=== ЗАДАНИЕ 2.12 ===")
    V1 = float(input("Введите скорость первого автомобиля (км/ч): "))
    V2 = float(input("Введите скорость второго автомобиля (км/ч): "))
    S = float(input("Введите начальное расстояние (км): "))
    T = float(input("Введите время (ч): "))
    
    distance = S + (V1 + V2) * T
    
    print(f"Расстояние через {T} часов = {distance} км")
    return distance

def task2_13():
    print("\n=== ЗАДАНИЕ 2.13 ===")
    A = float(input("Введите точку A: "))
    B = float(input("Введите точку B: "))
    C = float(input("Введите точку C: "))
    
    AC = abs(C - A)
    BC = abs(C - B)
    sum_lengths = AC + BC
    
    print(f"Длина AC = {AC}")
    print(f"Длина BC = {BC}")
    print(f"Сумма длин = {sum_lengths}")
    return AC, BC, sum_lengths

def task2_14():
    print("\n=== ЗАДАНИЕ 2.14 ===")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    
    sum_squares = a**2 + b**2
    diff_squares = a**2 - b**2
    prod_squares = a**2 * b**2
    quot_squares = a**2 / b**2
    
    print(f"Сумма квадратов = {sum_squares}")
    print(f"Разность квадратов = {diff_squares}")
    print(f"Произведение квадратов = {prod_squares}")
    print(f"Частное квадратов = {quot_squares}")
    return sum_squares, diff_squares, prod_squares, quot_squares

def task2_15():
    print("\n=== ЗАДАНИЕ 2.15 ===")
    V = float(input("Введите скорость лодки в стоячей воде (км/ч): "))
    U = float(input("Введите скорость течения реки (км/ч): "))
    T1 = float(input("Введите время движения по озеру (ч): "))
    T2 = float(input("Введите время движения против течения (ч): "))
    
    S_lake = V * T1
    S_river = (V - U) * T2
    S_total = S_lake + S_river
    
    print(f"Путь по озеру = {S_lake} км")
    print(f"Путь по реке = {S_river} км")
    print(f"Общий путь = {S_total} км")
    return S_total

# Главная программа
def main():
    print("Выберите задание (2.1-2.15):")
    choice = input()
    
    if choice == '2.1':
        result = task2_1()
    elif choice == '2.2':
        result = task2_2()
    elif choice == '2.3':
        result = task2_3()
    elif choice == '2.4':
        result = task2_4()
    elif choice == '2.5':
        result = task2_5()
    elif choice == '2.6':
        result = task2_6()
    elif choice == '2.7':
        result = task2_7()
    elif choice == '2.8':
        result = task2_8()
    elif choice == '2.9':
        result = task2_9()
    elif choice == '2.10':
        result = task2_10()
    elif choice == '2.11':
        result = task2_11()
    elif choice == '2.12':
        result = task2_12()
    elif choice == '2.13':
        result = task2_13()
    elif choice == '2.14':
        result = task2_14()
    elif choice == '2.15':
        result = task2_15()
    else:
        print("Неверный выбор!")
        return
    
    print("\nРезультат:", result)

if __name__ == "__main__":
    main()