#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = len(my_list)
    b = my_list.copy()
    if idx < 0:
        return b
    elif idx >= a:
        return b
    else:
        for i in range(a):
            if i == idx:
                b[i] = element
                return b
