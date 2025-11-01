#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    # Delete the element by slicing
    my_list[idx:idx+1] = []
    return my_list
