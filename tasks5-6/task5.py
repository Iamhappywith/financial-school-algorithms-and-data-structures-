import math

# ЗАДАНИЕ 5

# 1. Сумма дробей 1/2 + 1/2^2 + ... + 1/2^n
def task1(n):
    total = 0
    for i in range(1, n + 1):
        total += 1 / (2 ** i)
    return total

# 2. Сумма cos(x) + cos^2(x)/2 + ... + cos^n(x)/n
# def task2(n, x):
#     total = 0
#     for i in range(1, n + 1):
#         total += (math.cos(x) ** i) / i
#     return total

# # 3. Сумма 1 - 3 + 3^2 - 3^3 + ... + (-1)^n * 3^n
# def task3(n):
#     total = 0
#     for i in range(n + 1):
#         total += ((-1) ** i) * (3 ** i)
#     return total

# # 4. Сумма 1/sin(1) + 1/sin(2) + ... + 1/sin(n)
# def task4(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += 1 / math.sin(i)
#     return total

# # 5. Сумма 1 - 2^3 + 3^3 - ... + (-1)^(n+1) * n^3
# def task5(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += ((-1) ** (i + 1)) * (i ** 3)
#     return total

# # 6. Сумма cos(1) - cos(2) + cos(3) - ... + (-1)^(n+1) * cos(n)
# def task6(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += ((-1) ** (i + 1)) * math.cos(i)
#     return total

# # 7. Сумма x - x^2/2 + x^3/3 - ... + (-1)^(n-1) * x^n/n
# def task7(n, x):
#     total = 0
#     for i in range(1, n + 1):
#         total += ((-1) ** (i - 1)) * (x ** i) / i
#     return total

# # 8. Сумма 1! - 2! + 3! - ... + (-1)^(n+1) * n!
# def task8(n):
#     total = 0
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#         total += ((-1) ** (i + 1)) * factorial
#     return total

# # 9. Сумма sin(x) + sin(x^2) + ... + sin(x^n)
# def task9(n, x):
#     total = 0
#     for i in range(1, n + 1):
#         total += math.sin(x ** i)
#     return total

# # 10. Сумма 1 + 1/2! + 1/3! + ... + 1/n!
# def task10(n):
#     total = 0
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#         total += 1 / factorial
#     return total

# # 11. Сумма n^2 + (n+1)^2 + ... + (2n)^2
# def task11(n):
#     total = 0
#     for i in range(n, 2 * n + 1):
#         total += i ** 2
#     return total

# # 12. Сумма 1! + 2! + 3! + ... + n!
# def task12(n):
#     total = 0
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#         total += factorial
#     return total

# # 13. Сумма 1 + x + x^2/2! + x^3/3! + ... + x^n/n!
# def task13(n, x):
#     total = 1  # начинаем с 1
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#         total += (x ** i) / factorial
#     return total

# # 14. Сумма 1 - x + x^2 - x^3 + ... + (-1)^n * x^n
# def task14(n, x):
#     total = 0
#     for i in range(n + 1):
#         total += ((-1) ** i) * (x ** i)
#     return total

# # 15. Сумма x - x^3/3 + x^5/5 - ... + (-1)^n * x^(2n+1)/(2n+1)
# def task15(n, x):
#     total = 0
#     for i in range(n + 1):
#         total += ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
#     return total



n = int(input())
x = int(input())

result = task1(n)
print(result)
