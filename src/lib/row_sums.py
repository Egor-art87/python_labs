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