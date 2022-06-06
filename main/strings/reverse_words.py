def reverse_words_alternative(string):
    words = string.split(".")

    word_count = len(words)
    for index in range(int(word_count / 2)):
        words[index], words[word_count - index - 1] = words[word_count - index - 1], words[index]

    return ".".join(words)


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:

    # My solution for https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1
    # Function to reverse words in a given string.
    def reverseWords(self, S):
        words = S.split(".")
        words.reverse()
        return ".".join(words)
