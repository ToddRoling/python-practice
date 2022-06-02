def reverse_slice(string):
    return string[::-1]


def traverse_from_both_ends(string):
    left_index = 0
    right_index = len(string) - 1
    string_as_list = list(string)

    while left_index < right_index:
        temp = string_as_list[left_index]
        string_as_list[left_index] = string_as_list[right_index]
        string_as_list[right_index] = temp
        left_index += 1
        right_index -= 1

    return ''.join(string_as_list)


def traverse_to_midpoint(string):
    string_range = range(int(len(string) / 2))
    right_index = len(string) - 1
    string_as_list = list(string)

    for left_index in string_range:
        temp = string_as_list[left_index]
        string_as_list[left_index] = string_as_list[right_index]
        string_as_list[right_index] = temp
        right_index -= 1

    return ''.join(string_as_list)


print(traverse_to_midpoint("hello"))
