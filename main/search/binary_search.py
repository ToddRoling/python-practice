def binary_search(list_, target):

    first_index = 0
    last_index = len(list_) - 1

    while first_index <= last_index:
        middle_index = int((first_index + last_index) / 2)
        if list_[middle_index] == target:
            return middle_index
        elif list_[middle_index] < target:
            first_index = middle_index + 1
        else:
            last_index = middle_index - 1

    return -1
