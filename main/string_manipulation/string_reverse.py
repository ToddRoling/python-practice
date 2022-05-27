def reverse_slice(string):
    return string[::-1]


def traverse_from_both_ends(string):
    left_index = 0
    right_index = len(string) - 1

    while left_index < right_index:
        temp = string[left_index]
        string[left_index] = string[right_index]
        string[right_index] = temp
        left_index += 1
        right_index -= 1

    return string


def traverse_to_midpoint(string):
    string_range = range(int(len(string) / 2))
    string_end_index = len(string) - 1

    for left_index in string_range:
        right_index = string_end_index - left_index
        temp = string[left_index]
        string[left_index] = string[right_index]
        string[right_index] = temp

    return string
