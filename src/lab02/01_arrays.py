# тест кейсы
#  min_max

list1 = [3, -1, 5, 5, 0] # (-1, 5)
list2 = [42] # (42, 42)
list3 = [-5, -2, -9] # (-9, -2)
list4 = [] # ValueError
list5 = [1.5, 2, 2.0, -3.1] # (-3.1, 2)

# unique_sorted
list6 = [3, 1, 2, 1, 3] # [1, 2, 3]
list7 = [] # []
list8 = [-1, -1, 0, 2, 2] # [-1, 0, 2]
list9 = [1.0, 1, 2.5, 2.5, 0] # [0, 1.0, 2.5]

# flatten
list10 = [[1, 2], [3, 4]] # [1, 2, 3, 4]
list11 = ([1, 2], (3, 4, 5)) # [1, 2, 3, 4, 5]
list12 = [[1], [], [2, 3]] # [1, 2, 3]
list13 = [[1, 2], "ab"] # TypeError

# 1
def min_max_iz_spiska(my_list):
    if len(my_list) > 0:
        my_list = sorted(my_list)
        minn = my_list[-1]
        maxx = my_list[0]
        min_max= []
        min_max.append(maxx)
        min_max.append(minn)
        return tuple(min_max)
    else:
        return ValueError

print(min_max_iz_spiska(list1))
print(min_max_iz_spiska(list2))
print(min_max_iz_spiska(list3))
print(min_max_iz_spiska(list4))
print(min_max_iz_spiska(list5))

#2
print(list(sorted(dict.fromkeys(list6))))
print(list(sorted(dict.fromkeys(list7))))
print(list(sorted(dict.fromkeys(list8))))
print(list(sorted(dict.fromkeys(list9))))

#3
def raspl_row_major(elementary_list):
    result = []
    for i in elementary_list:
        if isinstance(i, (list, tuple)):
            result.extend(i)
        else:
            return TypeError(f'Элемент {i} не является списком или кортежем')
    return result

print(raspl_row_major(list10))
print(raspl_row_major(list11))
print(raspl_row_major(list12))
print(raspl_row_major(list13))