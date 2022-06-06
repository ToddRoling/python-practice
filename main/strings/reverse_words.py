def reverse_words_alternative(string):
    words = string.split(".")

    word_count = len(words)
    range_ = int(word_count / 2)
    for first_index in range(range_):
        last_index = word_count - first_index - 1
        words[first_index], words[last_index] = words[last_index], words[first_index]

    return ".".join(words)


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:

    # My solution for https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1
    # Function to reverse words in a given string.
    def reverseWords(self, S):
        words = S.split(".")
        words.reverse()
        return ".".join(words)
