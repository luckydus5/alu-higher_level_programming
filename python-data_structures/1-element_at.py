#!/usr/bin/python3
def element_at(my_list, idx):
    """Return the element at index idx in a list, or None if idx is invalid."""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
