def reverse_string_zero(string):
    return string[::-1]


def reverse_string_one(string):
    char_list = list(string)
    left_index = 0
    right_index = len(string) - 1

    while left_index < right_index:
        temp = char_list[left_index]
        char_list[left_index] = char_list[right_index]
        char_list[right_index] = temp
        left_index += 1
        right_index -= 1

    return ''.join(char_list)


def reverse_string_two(string):
    char_list = list(string)
    string_range = range(int(len(string) / 2))
    string_end_index = len(string) - 1

    for left_index in string_range:
        right_index = string_end_index - left_index
        temp = char_list[left_index]
        char_list[left_index] = char_list[right_index]
        char_list[right_index] = temp

    return ''.join(char_list)
