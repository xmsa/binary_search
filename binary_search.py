from isSort import is_sort


def recursive_binary_search(lst, value):
    """
    Recursive binary search
    Parameters:
        lst: list
            The list
        value: int,float, ...
            Search value

    Returns:
        int:
        index of element in list
        If it does not find the desired value, it returns -1
    """
    if len(lst) == 0:
        return -1

    median = int(len(lst) // 2)
    if lst[median] == value:
        return median
    elif lst[median] < value:
        flag = recursive_binary_search(lst[median + 1 :], value)
        if flag == -1:
            return -1
        return flag + median + 1
    elif lst[median] > value:
        return recursive_binary_search(lst[:median], value)
    else:
        return -1


def non_recursive_binary_search(lst, value):
    """
    non-Recursive binary search
    Parameters:
        lst: list
            The list
        value: int,float, ...
            Search value

    Returns:
        int:
        index of element in list
        If it does not find the desired value, it returns -1
    """
    i, j = 0, len(lst)
    while i < j:
        median = (i + j) // 2

        if lst[median] == value:
            return median
        elif lst[median] < value:
            i = median + 1
        elif lst[median] > value:
            j = median
        else:
            return -1
    return -1


def binary_search(lst, value, recursive=False):
    """
    Parameters:
        lst: list

        value: int,float, ...
            Search value
        recursive: bool (Defult:False)
            Recursive(True) and non-recursive(False)

    Returns:
        int:
        index of element in list
        If it does not find the desired value, it returns -1
    """

    if not (is_sort(lst)):
        print("The ascending list is not sort")
        return -1
    if recursive():
        return recursive_binary_search(lst, value)
    else:
        return non_recursive_binary_search(lst, value)
