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