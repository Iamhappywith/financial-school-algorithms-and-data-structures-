# ЗАДАНИЕ 15. МАТРИЦЫ И СТРОКИ (15 задач)

def task1():
    print("\n=== ЗАДАНИЕ 1 ===")
    def RemoveRowCol(A, K, L):
        M = len(A)
        N = len(A[0])
        
        if K > M or L > N:
            print("K или L превышают размеры матрицы")
            return A
        
        # Создаем новую матрицу без строки K и столбца L
        new_matrix = []
        for i in range(M):
            if i != K - 1:  # -1 потому что нумерация с 1
                new_row = []
                for j in range(N):
                    if j != L - 1:  # -1 потому что нумерация с 1
                        new_row.append(A[i][j])
                new_matrix.append(new_row)
        
        return new_matrix
    
    print("Введите размеры матрицы M и N:")
    M = int(input("M = "))
    N = int(input("N = "))
    
    print("Введите матрицу построчно:")
    A = []
    for i in range(M):
        row = list(map(int, input(f"Строка {i+1}: ").split()))
        A.append(row)
    
    print("Введите K и L (номера строки и столбца для удаления):")
    K = int(input("K = "))
    L = int(input("L = "))
    
    print("Исходная матрица:")
    for row in A:
        print(row)
    
    result = RemoveRowCol(A, K, L)
    
    print("Матрица после удаления:")
    for row in result:
        print(row)
    
    return result

def task2():
    print("\n=== ЗАДАНИЕ 2 ===")
    def Split(A):
        B = []  # четные числа
        C = []  # нечетные числа
        
        for num in A:
            if num % 2 == 0:
                B.append(num)
            else:
                C.append(num)
        
        return B, C
    
    print("Введите список чисел через пробел:")
    A = list(map(int, input().split()))
    
    B, C = Split(A)
    
    print(f"Исходный список: {A}")
    print(f"Четные числа: {B}")
    print(f"Нечетные числа: {C}")
    
    return B, C

def task3():
    print("\n=== ЗАДАНИЕ 3 ===")
    def SwapRow(A, K1, K2):
        M = len(A)
        
        if K1 > M or K2 > M:
            print("K1 или K2 превышают количество строк")
            return A
        
        # Меняем строки местами
        A[K1-1], A[K2-1] = A[K2-1], A[K1-1]
        return A
    
    print("Введите размеры матрицы M и N:")
    M = int(input("M = "))
    N = int(input("N = "))
    
    print("Введите матрицу построчно:")
    A = []
    for i in range(M):
        row = list(map(float, input(f"Строка {i+1}: ").split()))
        A.append(row)
    
    print("Введите K1 и K2 (номера строк для обмена):")
    K1 = int(input("K1 = "))
    K2 = int(input("K2 = "))
    
    print("Исходная матрица:")
    for row in A:
        print(row)
    
    result = SwapRow(A, K1, K2)
    
    print("Матрица после обмена строк:")
    for row in result:
        print(row)
    
    return result

def task4():
    print("\n=== ЗАДАНИЕ 4 ===")
    def Transp(A):
        M = len(A)
        # Создаем новую матрицу для результата
        result = []
        for i in range(M):
            new_row = []
            for j in range(M):
                new_row.append(A[j][i])
            result.append(new_row)
        return result
    
    print("Введите порядок матрицы M:")
    M = int(input("M = "))
    
    print("Введите матрицу построчно:")
    A = []
    for i in range(M):
        row = list(map(float, input(f"Строка {i+1}: ").split()))
        A.append(row)
    
    print("Исходная матрица:")
    for row in A:
        print(row)
    
    result = Transp(A)
    
    print("Транспонированная матрица:")
    for row in result:
        print(row)
    
    return result

def task5():
    print("\n=== ЗАДАНИЕ 5 ===")
    def MatrProd(A, B):
        rows_A = len(A)
        cols_A = len(A[0])
        rows_B = len(B)
        cols_B = len(B[0])
        
        if cols_A != rows_B:
            print("Ошибка: размеры матриц не совместимы для умножения")
            return None
        
        # Создаем результирующую матрицу
        result = []
        for i in range(rows_A):
            row = []
            for j in range(cols_B):
                sum_val = 0
                for k in range(cols_A):
                    sum_val += A[i][k] * B[k][j]
                row.append(sum_val)
            result.append(row)
        
        return result
    
    print("Введите размеры первой матрицы M1 и N1:")
    M1 = int(input("M1 = "))
    N1 = int(input("N1 = "))
    
    print("Введите первую матрицу построчно:")
    A = []
    for i in range(M1):
        row = list(map(float, input(f"Строка {i+1}: ").split()))
        A.append(row)
    
    print("Введите размеры второй матрицы M2 и N2:")
    M2 = int(input("M2 = "))
    N2 = int(input("N2 = "))
    
    print("Введите вторую матрицу построчно:")
    B = []
    for i in range(M2):
        row = list(map(float, input(f"Строка {i+1}: ").split()))
        B.append(row)
    
    result = MatrProd(A, B)
    
    if result:
        print("Результат умножения матриц:")
        for row in result:
            print(row)
    
    return result

def task6():
    print("\n=== ЗАДАНИЕ 6 ===")
    def SumMatr(A, B):
        rows_A = len(A)
        cols_A = len(A[0])
        rows_B = len(B)
        cols_B = len(B[0])
        
        if rows_A != rows_B or cols_A != cols_B:
            print("Ошибка: размеры матриц не совпадают")
            return None
        
        # Создаем результирующую матрицу
        result = []
        for i in range(rows_A):
            row = []
            for j in range(cols_A):
                row.append(A[i][j] + B[i][j])
            result.append(row)
        
        return result
    
    print("Введите размеры матриц M и N:")
    M = int(input("M = "))
    N = int(input("N = "))
    
    print("Введите первую матрицу построчно:")
    A = []
    for i in range(M):
        row = list(map(float, input(f"Строка {i+1}: ").split()))
        A.append(row)
    
    print("Введите вторую матрицу построчно:")
    B = []
    for i in range(M):
        row = list(map(float, input(f"Строка {i+1}: ").split()))
        B.append(row)
    
    result = SumMatr(A, B)
    
    if result:
        print("Результат сложения матриц:")
        for row in result:
            print(row)
    
    return result

def task7():
    print("\n=== ЗАДАНИЕ 7 ===")
    def DiagSum(A, diag_type):
        M = len(A)
        total = 0
        
        if diag_type == "main":
            # Сумма главной диагонали
            for i in range(M):
                total += A[i][i]
        else:
            # Сумма побочной диагонали
            for i in range(M):
                total += A[i][M-1-i]
        
        return total
    
    print("Введите порядок квадратной матрицы M:")
    M = int(input("M = "))
    
    print("Введите матрицу построчно:")
    A = []
    for i in range(M):
        row = list(map(float, input(f"Строка {i+1}: ").split()))
        A.append(row)
    
    print("Выберите диагональ:")
    print("1 - главная")
    print("2 - побочная")
    choice = input("Ваш выбор: ")
    
    if choice == "1":
        diag_type = "main"
    else:
        diag_type = "side"
    
    result = DiagSum(A, diag_type)
    print(f"Сумма элементов {diag_type} диагонали: {result}")
    
    return result

def task8():
    print("\n=== ЗАДАНИЕ 8 ===")
    def RemoveRows(A, K1, K2):
        M = len(A)
        
        if K1 > M:
            print("K1 превышает количество строк")
            return A
        
        if K2 > M:
            K2 = M
        
        # Создаем новую матрицу без указанных строк
        new_matrix = []
        for i in range(M):
            if i < K1 - 1 or i > K2 - 1:  # -1 потому что нумерация с 1
                new_matrix.append(A[i])
        
        return new_matrix
    
    print("Введите размеры матрицы M и N:")
    M = int(input("M = "))
    N = int(input("N = "))
    
    print("Введите матрицу построчно:")
    A = []
    for i in range(M):
        row = list(map(float, input(f"Строка {i+1}: ").split()))
        A.append(row)
    
    print("Введите K1 и K2 (номера строк для удаления):")
    K1 = int(input("K1 = "))
    K2 = int(input("K2 = "))
    
    print("Исходная матрица:")
    for row in A:
        print(row)
    
    result = RemoveRows(A, K1, K2)
    
    print("Матрица после удаления строк:")
    for row in result:
        print(row)
    
    return result

def task9():
    print("\n=== ЗАДАНИЕ 9 ===")
    def InvertStr(S, K, N):
        if K > len(S):
            return ""
        
        # Определяем подстроку для инвертирования
        if K + N > len(S):
            substr = S[K-1:]
        else:
            substr = S[K-1:K-1+N]
        
        # Возвращаем инвертированную подстроку
        return substr[::-1]
    
    print("Введите строку S:")
    S = input("S = ")
    
    print("Введите K и N:")
    K = int(input("K = "))
    N = int(input("N = "))
    
    result = InvertStr(S, K, N)
    print(f"Инвертированная подстрока: '{result}'")
    
    return result

def task10():
    print("\n=== ЗАДАНИЕ 10 ===")
    def SwapCol(A, K1, K2):
        M = len(A)
        N = len(A[0])
        
        if K1 > N or K2 > N:
            print("K1 или K2 превышают количество столбцов")
            return A
        
        # Меняем столбцы местами
        for i in range(M):
            A[i][K1-1], A[i][K2-1] = A[i][K2-1], A[i][K1-1]
        
        return A
    
    print("Введите размеры матрицы M и N:")
    M = int(input("M = "))
    N = int(input("N = "))
    
    print("Введите матрицу построчно:")
    A = []
    for i in range(M):
        row = list(map(float, input(f"Строка {i+1}: ").split()))
        A.append(row)
    
    print("Введите K1 и K2 (номера столбцов для обмена):")
    K1 = int(input("K1 = "))
    K2 = int(input("K2 = "))
    
    print("Исходная матрица:")
    for row in A:
        print(row)
    
    result = SwapCol(A, K1, K2)
    
    print("Матрица после обмена столбцов:")
    for row in result:
        print(row)
    
    return result

def task11():
    print("\n=== ЗАДАНИЕ 11 ===")
    def CompressStr(S):
        if not S:
            return ""
        
        result = ""
        count = 1
        current_char = S[0]
        
        for i in range(1, len(S)):
            if S[i] == current_char:
                count += 1
            else:
                if count > 4:
                    result += f"{current_char}{{{count}}}"
                else:
                    result += current_char * count
                current_char = S[i]
                count = 1
        
        # Обрабатываем последнюю последовательность
        if count > 4:
            result += f"{current_char}{{{count}}}"
        else:
            result += current_char * count
        
        return result
    
    print("Введите строку S:")
    S = input("S = ")
    
    result = CompressStr(S)
    print(f"Сжатая строка: '{result}'")
    
    return result

def task12():
    print("\n=== ЗАДАНИЕ 12 ===")
    def IsIdent(S):
        if not S:
            return False
        
        # Проверяем первый символ
        first_char = S[0]
        if not (first_char.isalpha() or first_char == '_'):
            return False
        
        # Проверяем остальные символы
        for char in S:
            if not (char.isalnum() or char == '_'):
                return False
        
        return True
    
    print("Введите строку для проверки:")
    S = input("S = ")
    
    result = IsIdent(S)
    print(f"Строка '{S}' является идентификатором: {result}")
    
    return result

def task13():
    print("\n=== ЗАДАНИЕ 13 ===")
    def Chessboard(M, N):
        # Создаем матрицу M x N
        A = []
        for i in range(M):
            row = []
            for j in range(N):
                # Чередуем 0 и 1 в шахматном порядке
                if (i + j) % 2 == 0:
                    row.append(0)
                else:
                    row.append(1)
            A.append(row)
        return A
    
    print("Введите M и N:")
    M = int(input("M = "))
    N = int(input("N = "))
    
    result = Chessboard(M, N)
    
    print("Шахматная матрица:")
    for row in result:
        print(row)
    
    return result

def task14():
    print("\n=== ЗАДАНИЕ 14 ===")
    def Bell(L):
        if not L:
            return []
        
        # Сортируем список
        sorted_L = sorted(L)
        result = []
        
        # Чередуем добавление с начала и с конца
        left = 0
        right = len(sorted_L) - 1
        
        while left <= right:
            if left == right:
                result.append(sorted_L[left])
            else:
                result.append(sorted_L[left])
                result.append(sorted_L[right])
            left += 1
            right -= 1
        
        return result
    
    print("Введите список чисел через пробел:")
    L = list(map(int, input().split()))
    
    result = Bell(L)
    print(f"Исходный список: {L}")
    print(f"Список в форме колокола: {result}")
    
    return result

def task15():
    print("\n=== ЗАДАНИЕ 15 ===")
    def RemoveCols(A, K1, K2):
        M = len(A)
        N = len(A[0])
        
        if K1 > N:
            print("K1 превышает количество столбцов")
            return A
        
        if K2 > N:
            K2 = N
        
        # Создаем новую матрицу без указанных столбцов
        new_matrix = []
        for i in range(M):
            new_row = []
            for j in range(N):
                if j < K1 - 1 or j > K2 - 1:  # -1 потому что нумерация с 1
                    new_row.append(A[i][j])
            new_matrix.append(new_row)
        
        return new_matrix
    
    print("Введите размеры матрицы M и N:")
    M = int(input("M = "))
    N = int(input("N = "))
    
    print("Введите матрицу построчно:")
    A = []
    for i in range(M):
        row = list(map(float, input(f"Строка {i+1}: ").split()))
        A.append(row)
    
    print("Введите K1 и K2 (номера столбцов для удаления):")
    K1 = int(input("K1 = "))
    K2 = int(input("K2 = "))
    
    print("Исходная матрица:")
    for row in A:
        print(row)
    
    result = RemoveCols(A, K1, K2)
    
    print("Матрица после удаления столбцов:")
    for row in result:
        print(row)
    
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