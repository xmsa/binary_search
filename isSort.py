def is_sort(lst, ascending=True):
    """
    Checks whether the presentation is ascending or descending
    Parameters:
        lst: list
            The list
        ascending: bool, default=True
            Determining ascending or descending

    Returns:
        bool:
        If the list was in order, "true", otherwise "false"
    """
    flag = 0
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1] and ascending:

            return False
        elif lst[i] < lst[i + 1] and not (ascending):
            return False

    return True

