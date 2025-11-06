# transpose
lst1 = [[1, 2, 3]] # [[1], [2], [3]]
lst2 = [[1], [2], [3]] # [[1, 2, 3]]
lst3 = [[1, 2], [3, 4]] # [[1, 3], [2, 4]]
lst4 = []             # []
lst5 = [[1, 2], [3]] # ValueError (рваная матрица)

# row_sums
lst6 = [[1, 2, 3], [4, 5, 6]] # [6, 15]
lst7 = [[-1, 1], [10, -10]] # [0, 0]
lst8 = [[0, 0], [0, 0]] # [0, 0]
lst9 = [[1, 2], [3]] # ValueError

# col_sums
lst10 = [[1, 2, 3], [4, 5, 6]] # [5, 7, 9]
lst11 = [[-1, 1], [10, -10]] # [9, -9]
lst12 = [[0, 0], [0, 0]] #[0, 0]
lst13 = [[1, 2], [3]] # ValueError

# 1

def transpose_compact(mat):
    if not mat:
        return []  # возращаю пустой список, если матрица пустая
    # проверяю, что матрица не рванная
    first_row = len(mat[0]) # беру эталонное значение 
    for row in mat: 
        if len(row) != first_row: # если длина row != этлону - ошибка 
            return ValueError('рванная')
        # формирую новую матрицу 
    res = []               # создаю пустой список 
    # определяю размеры исходной матрицы 
    num_cols = len(mat[0])  # кол-во столбцов 
    num_rows = len(mat)     # кол-во строк

    for col in range(num_cols): # прохожусь по всем стодбцам 
        new_row = []  # промежуточный список 
        for row in range(num_rows):  # прохожусь по всем строкам 
            new_row.append(mat[row][col])  # добавляю в новый список строки и стобцы 
        res.append(new_row) # добавляю промежуточный списко в конечный 
    return res   # возвращаю результат 

print('transpose')
print(transpose_compact(lst1))
print(transpose_compact(lst2))
print(transpose_compact(lst3))
print(transpose_compact(lst4))
print(transpose_compact(lst5))

# 2
def row_sums(matr):  
    if not matr:      # проверяю матрицу на пустоту 
        return []      # возвращаю пустой списк 
    row1 = len(matr[0])     
    for i in matr:            # проверка на рванность 
        if len(i) != row1:      
            return ValueError('Рванная матрица')
    sums = []              
    for rows in matr:      # прохожусь по строкам 
        row_sum = 0      # счетчик
        for element in rows:    # прохожусь по каждому значению строки 
            row_sum += element  # добавляю его в счетчик 
        sums.append(row_sum)   # добавляю в конечный список 
    return sums     # возвращаю результат 

print('row_sums')
print(row_sums(lst6))
print(row_sums(lst7))
print(row_sums(lst8))
print(row_sums(lst9))
            
# 3

def col_sums(matrix):
    if not matrix:
        return []              # проверка 
    row_first = len(matrix[0])    
    for r in matrix:
        if len(r) != row_first:
            return ValueError('рванная')
    num_cols = len(matrix[0])
    res = []
    for col_index in range(num_cols):      # тоже самое, что и в поиске суммы строки, только наоборот 
        col_sum = 0
        for r in matrix:
            col_sum += r[col_index]
        res.append(col_sum)
    return res

print('col_sums')
print(col_sums(lst10))
print(col_sums(lst11))
print(col_sums(lst12))
print(col_sums(lst13))
    
    
    
        


