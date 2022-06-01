# My solution for https://practice.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1
class Solution:

    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def longestCommonPrefix(self, arr, n):
        if not arr:
            return -1
        if len(arr) == 1:
            return arr[0] if arr[0] else -1

        def _get_common_prefix(string_one_, string_two):
            minimum_length = min(len(string_one_), len(string_two))
            prefix_ = ''
            for index_ in range(minimum_length):
                if string_one_[index_] == string_two[index_]:
                    prefix_ += string_one_[index_]
                else:
                    break
            return prefix_

        prefix = ''
        for index in range(n - 1):
            string_one = prefix if prefix else arr[index]
            prefix = _get_common_prefix(string_one, arr[index + 1])
            if not prefix:
                break

        return prefix if prefix else -1
