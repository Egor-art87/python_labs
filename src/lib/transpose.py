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
