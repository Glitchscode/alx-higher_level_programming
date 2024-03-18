#!/usr/bin/python3
"""Print the sum of 1 and 2."""
"""def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{}".format(my_list[i]))"""
def print_list_integer(my_list=[]):
    a = [print("{}".format(my_list[i])) for i in range(len(my_list))]
