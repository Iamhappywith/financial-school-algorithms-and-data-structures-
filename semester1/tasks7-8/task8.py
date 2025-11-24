# ЗАДАНИЕ 8. Вложенные списки

# 1. Дана целочисленная матрица размера M × N. Найти номер первого из ее столбцов, содержащих только нечетные числа.
def task8_1(matrix):
    M = len(matrix)
    if M == 0:
        return 0
    N = len(matrix[0])
    
    for j in range(N):
        all_odd = True
        for i in range(M):
            if matrix[i][j] % 2 == 0:
                all_odd = False
                break
        if all_odd:
            return j + 1
    return 0

# 2. Дана матрица размера M × N. Преобразовать матрицу, поменяв местами минимальный и максимальный элемент в каждой строке.
def task8_2(matrix):
    result = [row[:] for row in matrix]
    
    for i in range(len(result)):
        if len(result[i]) > 0:
            min_val = min(result[i])
            max_val = max(result[i])
            min_idx = result[i].index(min_val)
            max_idx = result[i].index(max_val)
            result[i][min_idx], result[i][max_idx] = result[i][max_idx], result[i][min_idx]
    
    return result

# 3. Дана матрица размера M × N. Поменять местами строки, содержащие минимальный и максимальный элементы матрицы.
def task8_3(matrix):
    if not matrix:
        return matrix
    
    result = [row[:] for row in matrix]
    M, N = len(result), len(result[0])
    
    min_val = min(min(row) for row in result)
    max_val = max(max(row) for row in result)
    
    min_row_idx = -1
    max_row_idx = -1
    
    for i in range(M):
        if min_val in result[i]:
            min_row_idx = i
        if max_val in result[i]:
            max_row_idx = i
    
    if min_row_idx != -1 and max_row_idx != -1 and min_row_idx != max_row_idx:
        result[min_row_idx], result[max_row_idx] = result[max_row_idx], result[min_row_idx]
    
    return result

# 4. Дана матрица размера M × N. Зеркально отразить ее элементы относительно горизонтальной оси симметрии матрицы.
def task8_4(matrix):
    return matrix[::-1]

# 5. Дана матрица размера M × N. Удалить строку, содержащую минимальный элемент матрицы.
def task8_5(matrix):
    if not matrix:
        return matrix
    
    min_val = min(min(row) for row in matrix)
    
    for i in range(len(matrix)):
        if min_val in matrix[i]:
            return matrix[:i] + matrix[i+1:]
    
    return matrix

# 6. Дана матрица размера M × N. Удалить столбец, содержащий максимальный элемент матрицы.
def task8_6(matrix):
    if not matrix or not matrix[0]:
        return matrix
    
    M, N = len(matrix), len(matrix[0])
    max_val = matrix[0][0]
    max_col = 0
    
    for j in range(N):
        for i in range(M):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_col = j
    
    result = []
    for i in range(M):
        new_row = matrix[i][:max_col] + matrix[i][max_col+1:]
        result.append(new_row)
    
    return result

# 7. Дана матрица размера M × N. Зеркально отразить ее элементы относительно вертикальной оси симметрии матрицы.
def task8_7(matrix):
    return [row[::-1] for row in matrix]

# 8. Дана матрица размера M × N. Продублировать строку матрицы, содержащую ее максимальный элемент.
def task8_8(matrix):
    if not matrix:
        return matrix
    
    max_val = max(max(row) for row in matrix)
    
    for i in range(len(matrix)):
        if max_val in matrix[i]:
            return matrix[:i] + [matrix[i]] + matrix[i:]
    
    return matrix

# 9. Дана матрица размера M × N. В каждом ее столбце найти количество элементов, больших среднего арифметического всех элементов этого столбца.
def task8_9(matrix):
    if not matrix or not matrix[0]:
        return []
    
    M, N = len(matrix), len(matrix[0])
    result = []
    
    for j in range(N):
        column = [matrix[i][j] for i in range(M)]
        avg = sum(column) / M
        count = sum(1 for x in column if x > avg)
        result.append(count)
    
    return result

# 10. Дана матрица размера M × N (M и N — четные числа). Поменять местами левую верхнюю и правую нижнюю четверти матрицы.
def task8_10(matrix):
    M, N = len(matrix), len(matrix[0])
    
    if M % 2 != 0 or N % 2 != 0:
        raise ValueError("M и N должны быть четными числами")
    
    result = [row[:] for row in matrix]
    half_M, half_N = M // 2, N // 2
    
    for i in range(half_M):
        for j in range(half_N):
            result[i][j], result[i + half_M][j + half_N] = result[i + half_M][j + half_N], result[i][j]
    
    return result

# 11. Дана матрица размера M × N. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.
def task8_11(matrix):
    result = []
    
    for i in range(0, len(matrix), 2):
        if i < len(matrix):
            row_avg = sum(matrix[i]) / len(matrix[i]) if matrix[i] else 0
            result.append(row_avg)
    
    return result

# 12. Дана матрица размера M × N. Найти номер ее строки с наибольшей суммой элементов и вывести данный номер, а также значение наибольшей суммы.
def task8_12(matrix):
    if not matrix:
        return 0, 0
    
    max_sum = -float('inf')
    max_row_idx = 0
    
    for i in range(len(matrix)):
        row_sum = sum(matrix[i])
        if row_sum > max_sum:
            max_sum = row_sum
            max_row_idx = i + 1
    
    return max_row_idx, max_sum

# 13. Дана матрица размера M × N. Перед строкой матрицы, содержащей минимальный элемент матрицы, вставить строку из нулей.
def task8_13(matrix):
    if not matrix:
        return matrix
    
    min_val = min(min(row) for row in matrix)
    zero_row = [0] * len(matrix[0])
    
    for i in range(len(matrix)):
        if min_val in matrix[i]:
            return matrix[:i] + [zero_row] + matrix[i:]
    
    return matrix

# 14. Дана целочисленная матрица размера M × N. Найти номер последней из ее строк, содержащих только четные числа.
def task8_14(matrix):
    M = len(matrix)
    
    for i in range(M-1, -1, -1):
        all_even = True
        for element in matrix[i]:
            if element % 2 != 0:
                all_even = False
                break
        if all_even:
            return i + 1
    
    return 0

# 15. Дана матрица размера M × N. Поменять местами столбец с номером 1 и последний из столбцов, содержащих только положительные элементы.
def task8_15(matrix):
    if not matrix or not matrix[0]:
        return matrix
    
    M, N = len(matrix), len(matrix[0])
    result = [row[:] for row in matrix]
    
    last_positive_col = -1
    
    for j in range(N-1, -1, -1):
        all_positive = True
        for i in range(M):
            if matrix[i][j] <= 0:
                all_positive = False
                break
        if all_positive:
            last_positive_col = j
            break
    
    if last_positive_col != -1 and last_positive_col != 0:
        for i in range(M):
            result[i][0], result[i][last_positive_col] = result[i][last_positive_col], result[i][0]
    
    return result


# Пример использования:
lst = [12, -5, 8, 3, 17, -2, 25, 6, 10, 15, -8, 30]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print("Задание 8.1:", task8_1(matrix))
print("Задание 8.2:", task8_2(matrix))
print("Задание 8.4:", task8_4(matrix))