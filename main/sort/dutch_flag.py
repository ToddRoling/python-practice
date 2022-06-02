# noinspection PyMethodMayBeStatic
class Solution:

    # My solution for https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
    def sort012_v0(self, arr, n):

        valid_input = arr is not None and len(arr) == n
        if not valid_input:
            return None

        zeros_count = 0
        ones_count = 0

        for number in arr:
            if number == 0:
                zeros_count += 1
            if number == 1:
                ones_count += 1

        for index in range(n):
            if zeros_count > 0:
                arr[index] = 0
                zeros_count -= 1
            elif ones_count > 0:
                arr[index] = 1
                ones_count -= 1
            else:
                arr[index] = 2
        return arr

    # My alternative solution for https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
    def sort012_v1(self, arr, n):

        valid_input = arr is not None and len(arr) == n
        if not valid_input:
            return None

        last_zero_index = -1
        first_two_index = n
        unknown_range_index = 0
        while unknown_range_index < first_two_index:
            if arr[unknown_range_index] == 0:
                last_zero_index += 1
                temp = arr[last_zero_index]
                arr[last_zero_index] = arr[unknown_range_index]
                arr[unknown_range_index] = temp
                unknown_range_index += 1
            elif arr[unknown_range_index] == 1:
                unknown_range_index += 1
            else:
                first_two_index -= 1
                temp = arr[unknown_range_index]
                arr[unknown_range_index] = arr[first_two_index]
                arr[first_two_index] = temp
        return arr
