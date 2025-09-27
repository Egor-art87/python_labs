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
    num_cols = len(mat[0])  
    num_rows = len(mat)

    for col in range(num_cols):
        new_row = []
        for row in range(num_rows):
            new_row.append(mat[row][col])
        res.append(new_row)
    return res

print(transpose_compact(lst1))
print(transpose_compact(lst2))
print(transpose_compact(lst3))
print(transpose_compact(lst4))
print(transpose_compact(lst5))

# 2
def row_sums(matr):
    if not matr:
        return []
    row1 = len(matr[0])
    for i in matr:
        if len(i) != row1:
            return ValueError('Рванная матрица')
    sums = []
    for rows in matr:
        row_sum = 0
        for element in rows:
            row_sum += element
        sums.append(row_sum)
    return sums

print(row_sums(lst6))
print(row_sums(lst7))
print(row_sums(lst8))
print(row_sums(lst9))
            
# 3

def col_sums(matrix):
    if not matrix:
        return []
    row_first = len(matrix[0])
    for r in matrix:
        if len(r) != row_first:
            return ValueError('рванная')
    num_cols = len(matrix[0])
    res = []
    for col_index in range(num_cols):
        col_sum = 0
        for r in matrix:
            col_sum += r[col_index]
        res.append(col_sum)
    return res

print(col_sums(lst10))
print(col_sums(lst11))
print(col_sums(lst12))
print(col_sums(lst13))
    
    
    
        


