# My solution for https://practice.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1
class Solution:

    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def longestCommonPrefix(self, arr, n):
        if not arr:
            return -1
        if len(arr) == 1:
            return arr[0]

        prefix = min(arr, key=len)
        arr.remove(prefix)

        common_prefix_found = False
        while not common_prefix_found and prefix:
            for string in arr:
                common_prefix_found = string.startswith(prefix)
                if not common_prefix_found:
                    prefix = prefix[:-1]
                    break

        return prefix if prefix else -1

