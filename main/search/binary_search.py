def binary_search(search_list, target):

    first_index = 0
    last_index = len(search_list) - 1

    while first_index <= last_index:
        middle_index = int((first_index + last_index) / 2)
        if search_list[middle_index] == target:
            return middle_index
        elif search_list[middle_index] < target:
            first_index = middle_index + 1
        else:
            last_index = middle_index - 1

    return -1
