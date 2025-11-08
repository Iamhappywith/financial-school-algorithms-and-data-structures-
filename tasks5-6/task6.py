import math

# ЗАДАНИЕ 6. СПИСКИ

# 1. Среднее арифметическое элементов с номерами от K до L
# def task1(lst, K, L):
#     k, l = K - 1, L - 1
#     selected = lst[k:l + 1]
#     return sum(selected) / len(selected)

# 2. Сумма всех элементов, кроме элементов с номерами от K до L
# def task2(lst, K, L):
#     k, l = K - 1, L - 1
#     total = 0
#     for i in range(len(lst)):
#         if i < k or i > l:
#             total += lst[i]
#     return total

# 3. Среднее арифметическое всех элементов, кроме элементов с номерами от K до L
# def task3(lst, K, L):
#     k, l = K - 1, L - 1
#     selected = []
#     for i in range(len(lst)):
#         if i < k or i > l:
#             selected.append(lst[i])
#     return sum(selected) / len(selected) if selected else 0

# 4. Четные числа по порядку, потом нечетные в обратном порядке
# def task4(lst):
#     even_numbers = []
#     odd_numbers = []
    
#     for num in lst:
#         if num % 2 == 0:
#             even_numbers.append(num)
#         else:
#             odd_numbers.append(num)
    
#     return even_numbers + odd_numbers[::-1]

# 5. Элементы с четными номерами, потом с нечетными номерами
def task5(lst):
    even_index = []
    odd_index = []
    
    for i in range(len(lst)):
        if (i + 1) % 2 == 0:  # четная позиция
            even_index.append(lst[i])
        else:  # нечетная позиция
            odd_index.append(lst[i])
    
    return even_index + odd_index

# 6. Произведение элементов после максимального
# def task6(lst):
#     if not lst:
#         return 0
    
#     max_index = lst.index(max(lst))
    
#     if max_index == len(lst) - 1:
#         return 0
    
#     product = 1
#     for i in range(max_index + 1, len(lst)):
#         product *= lst[i]
    
#     return product

# 7. Сумма между минимальным и максимальным элементами
# def task7(lst):
#     if not lst:
#         return 0
    
#     min_index = lst.index(min(lst))
#     max_index = lst.index(max(lst))
    
#     start = min(min_index, max_index)
#     end = max(min_index, max_index)
    
#     total = 0
#     for i in range(start, end + 1):
#         total += lst[i]
    
#     return total

# 8. Обнулить элементы между минимальным и максимальным
# def task8(lst):
#     if len(lst) < 3:
#         return lst
    
#     min_index = lst.index(min(lst))
#     max_index = lst.index(max(lst))
    
#     start = min(min_index, max_index)
#     end = max(min_index, max_index)
    
#     result = lst.copy()
#     for i in range(start + 1, end):
#         result[i] = 0
    
#     return result

# 9. Увеличить четные числа на заданное число
# def task9(lst, increment):
#     result = []
#     for num in lst:
#         if num % 2 == 0:
#             result.append(num + increment)
#         else:
#             result.append(num)
#     return result

# 10. Обнулить все нечетные числа
# def task10(lst):
#     result = []
#     for num in lst:
#         if num % 2 != 0:
#             result.append(0)
#         else:
#             result.append(num)
#     return result

# 11. Минимальный элемент среди элементов с четными номерами
# def task11(lst):
#     even_index_elements = []
#     for i in range(len(lst)):
#         if (i + 1) % 2 == 0:
#             even_index_elements.append(lst[i])
    
#     return min(even_index_elements) if even_index_elements else None

# 12. Элементы, которые больше правого соседа
# def task12(lst):
#     result_indices = []
#     count = 0
    
#     for i in range(len(lst) - 1):
#         if lst[i] > lst[i + 1]:
#             result_indices.append(i + 1)
#             count += 1
    
#     return result_indices, count

# 13. Два соседних элемента с максимальной суммой
# def task13(lst):
#     if len(lst) < 2:
#         return None
    
#     max_sum = lst[0] + lst[1]
#     result_pair = (lst[0], lst[1])
    
#     for i in range(len(lst) - 1):
#         current_sum = lst[i] + lst[i + 1]
#         if current_sum > max_sum:
#             max_sum = current_sum
#             result_pair = (lst[i], lst[i + 1])
    
#     return result_pair

# 14. Поменять местами минимальный и максимальный элементы
# def task14(lst):
#     if not lst:
#         return lst
    
#     result = lst.copy()
#     min_index = result.index(min(result))
#     max_index = result.index(max(result))
    
#     result[min_index], result[max_index] = result[max_index], result[min_index]
#     return result

# 15. Создать список по правилу
# def task15(N, A, B):
#     if N < 2:
#         return []
    
#     result = [A, B]
#     for i in range(2, N):
#         next_element = sum(result)
#         result.append(next_element)
    
#     return result



# Ввод данных
print("Введите элементы списка через пробел:")
lst_input = input().split()
lst = []
for item in lst_input:
    if '.' in item:
        lst.append(float(item))
    else:
        lst.append(int(item))

# # Дополнительный ввод для K и L
# K = int(input("Введите K: "))
# L = int(input("Введите L: "))

# Ввод данных для задачи 15
# N = int(input("Введите N (>2): "))
# A = int(input("Введите A: "))
# B = int(input("Введите B: "))

result = task5(lst) 
print(result)