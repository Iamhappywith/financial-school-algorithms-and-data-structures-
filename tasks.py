import math

# def task10(price):
#     weight = 1.0
#     while weight <= 2.0:
#         print(f"{weight} кг - {price * weight:.2f} руб.")
#         weight += 0.2


# task10(100)


def task13(N):
    K = 0
    while (K + 1)**2 <= N:
        K += 1
    print(f"Наибольшее K: {K}")

task13(10)
