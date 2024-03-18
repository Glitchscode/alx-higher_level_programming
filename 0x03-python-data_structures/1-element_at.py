#!/usr/bin/python3
def element_at(my_list, idx):
    a = len(my_list)
    b = my_list
    if idx < 0:
        return None
    elif idx >= a:
        return None
    else:
        for i in range(a):
            if i == idx:
                return b[i]
