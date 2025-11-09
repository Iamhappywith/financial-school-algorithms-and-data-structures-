# ЗАДАНИЕ 3

# 1
def task1(a, x):
    if x > 0:
        return a*x**2 + 1
    else:
        return a*x - 1


print(task1(4,3))

# # 2
# def task2(a, x):
#     if x >= 1:
#         return a*x + 1
#     else:
#         return x**2 - 1

# # 3
# def task3(a, x):
#     if x < 0:
#         return 3*a**2
#     else:
#         return 4*a*x - 1

# # 4
# def task4(a, x):
#     if x > 4:
#         return 2*a**2
#     else:
#         return 3*x - 1

# # 5
# def task5(a, x):
#     if x > 2:
#         return 2*a*x - 2
#     else:
#         return 3*a**2 - 2*x

# # 6
# def task6(a, x):
#     if x > 1:
#         return 2*a*x**2 - 1
#     else:
#         return x

# # 7
# def task7(a, x):
#     if x > 2:
#         return x**2
#     else:
#         return 2*a - 1

# # 8
# import math
# def task8(x):
#     if x > 2:
#         return math.cos(2*x - 1)
#     else:
#         return math.sin(3*x + 1)

# # 9
# def task9(x):
#     if x > 2:
#         return 2*x**3 - 2*x - 1
#     else:
#         return 3*x**2 - 2*x + 1

# # 10
# def task10(a, x):
#     if x > 1:
#         return 2*a*x**2 - 1
#     else:
#         return 1/a

# # 11
# def task11(a, x):
#     if x >= 0:
#         return a*math.sqrt(x) + 1
#     else:
#         return a*x - 1

# # 12
# def task12(a, x):
#     if x >= 0:
#         return math.sqrt(x) + a
#     else:
#         return a/x - 1

# # 13
# def task13(a, x):
#     if x > 0:
#         return 1/x + a
#     else:
#         return x**2 - 1

# # 14
# def task14(x):
#     if x > math.pi/2:
#         return math.cos(x)
#     else:
#         return math.sin(x)

# # 15
# def task15(x):
#     if x > 2:
#         return math.sqrt(x-2)
#     else:
#         return (x - 2)**2 + 1


# # ЗАДАНИЕ 4 

# # 1
# def task1(K, N):
#     for _ in range(N):
#         print(K)

# # 2
# def task2(A, B):
#     count = 0
#     for i in range(A, B + 1):
#         print(i)
#         count += 1
#     print("Количество чисел:", count)

# # 3
# def task3(A, B):
#     count = 0
#     for i in range(B - 1, A, -1):
#         print(i)
#         count += 1
#     print("Количество чисел:", count)

# # 4
# def task4():
#     price = 20.4
#     for i in range(1, 11):
#         print(f"{i} шт. - {price * i:.2f} руб.")

# # 5
# def task5(A, B, H):
#     for i in range(A, B + 1, H):
#         print(f"{i}^2 = {i**2}")

# # 6
# def task6(A, B, H):
#     for i in range(A, B + 1, H):
#         if i > 0:
#             print(i)

# # 7
# def task7(A, B):
#     total = 0
#     for i in range(A, B + 1):
#         total += i
#     print("Сумма:", total)

# # 8
# def task8(A, B):
#     product = 1
#     for i in range(A, B + 1):
#         product *= i
#     print("Произведение:", product)

# # 9
# def task9(A, B):
#     total = 0
#     for i in range(A, B + 1):
#         total += i**2
#     print("Сумма квадратов:", total)

# # 10
# def task10(price):
#     weight = 1.0
#     while weight <= 2.0:
#         print(f"{weight} кг - {price * weight:.2f} руб.")
#         weight += 0.2

# # 11
# def task11(N):
#     square = 0
#     for i in range(1, 2*N, 2):
#         square += i
#     print(f"{N}^2 = {square}")

# # 12
# def task12(A, N):
#     for i in range(1, N + 1):
#         print(f"{A}^{i} = {A**i}")

# # 13
# def task13(N):
#     K = 0
#     while (K + 1)**2 <= N:
#         K += 1
#     print(f"Наибольшее K: {K}")

# # 14
# def task14(N):
#     K = 0
#     power = 1
#     while 3**(K + 1) < N:
#         K += 1
#         power *= 3
#     print(f"Наибольшее K: {K}")

# # 15
# def task15(N, A, B):
#     H = (B - A) / N
#     print(f"Длина отрезка H: {H}")
    
#     current = A
#     points = []
#     for i in range(N + 1):
#         points.append(current)
#         current += H
    
#     print("Точки разбиения:", [round(p, 2) for p in points])
