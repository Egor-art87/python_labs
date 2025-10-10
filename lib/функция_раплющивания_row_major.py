def raspl_row_major(elementary_list):
    result = []
    for i in elementary_list:
        if isinstance(i, (list, tuple)):
            result.extend(i)
        else:
            return TypeError(f'Элемент {i} не является списком или кортежем')
    return result