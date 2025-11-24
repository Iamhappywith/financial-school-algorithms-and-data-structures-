# ЗАДАНИЕ 7. Сортировка списков

# 1. Дан список. Выбрать из списка все нечетные числа и упорядочить их по убыванию.
def task7_1(lst):
    result = [x for x in lst if x % 2 != 0]
    return sorted(result, reverse=True)

# 2. Дан список. Выбрать из списка все положительные числа и упорядочить их по возрастанию.
def task7_2(lst):
    result = [x for x in lst if x > 0]
    return sorted(result)

# 3. Дан список. Выбрать из списка все положительные числа и упорядочить их по убыванию.
def task7_3(lst):
    result = [x for x in lst if x > 0]
    return sorted(result, reverse=True)

# 4. Дан список. Выбрать из списка все четные числа и упорядочить их по возрастанию.
def task7_4(lst):
    result = [x for x in lst if x % 2 == 0]
    return sorted(result)

# 5. Дан список. Выбрать из списка все числа больше заданного числа k и упорядочить их по убыванию.
def task7_5(lst, k):
    result = [x for x in lst if x > k]
    return sorted(result, reverse=True)

# 6. Дан список. Выбрать из списка все числа больше 10 и упорядочить их по возрастанию.
def task7_6(lst):
    result = [x for x in lst if x > 10]
    return sorted(result)

# 7. Дан список. Выбрать из списка все числа кратные 5 и упорядочить их по убыванию.
def task7_7(lst):
    result = [x for x in lst if x % 5 == 0]
    return sorted(result, reverse=True)

# 8. Дан список. Выбрать из списка все числа меньше заданного числа k и упорядочить их по возрастанию.
def task7_8(lst, k):
    result = [x for x in lst if x < k]
    return sorted(result)

# 9. Дан список. Выбрать из списка все числа меньше 15 и упорядочить их по убыванию.
def task7_9(lst):
    result = [x for x in lst if x < 15]
    return sorted(result, reverse=True)

# 10. Дан список. Выбрать из списка все числа кратные 3 и упорядочить их по возрастанию.
def task7_10(lst):
    result = [x for x in lst if x % 3 == 0]
    return sorted(result)

# 11. Дан список. Выбрать из списка все числа кратные заданному числу k и упорядочить их по убыванию.
def task7_11(lst, k):
    result = [x for x in lst if x % k == 0]
    return sorted(result, reverse=True)

# 12. Дан список. Выбрать из списка все отрицательные числа и упорядочить их по возрастанию.
def task7_12(lst):
    result = [x for x in lst if x < 0]
    return sorted(result)

# 13. Дан список. Выбрать из списка все числа на нечетных позициях и упорядочить эти числа по убыванию.
def task7_13(lst):
    result = [lst[i] for i in range(len(lst)) if (i + 1) % 2 != 0]
    return sorted(result, reverse=True)

# 14. Дан список. Выбрать из списка все двузначные числа и упорядочить эти числа по возрастанию.
def task7_14(lst):
    result = [x for x in lst if 10 <= abs(x) <= 99]
    return sorted(result)

# 15. Дан список. Выбрать из списка все числа на четных позициях и упорядочить эти числа по возрастанию.
def task7_15(lst):
    result = [lst[i] for i in range(len(lst)) if (i + 1) % 2 == 0]
    return sorted(result)


# Пример использования:
lst = [12, -5, 8, 3, 17, -2, 25, 6, 10, 15, -8, 30]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Задание 7.1:", task7_1(lst))
print("Задание 7.2:", task7_2(lst))
print("Задание 7.4:", task7_4(lst))
