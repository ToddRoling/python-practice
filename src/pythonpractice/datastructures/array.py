def get_array_sum(array: list[int]):
    # instead of just sum(array)
    sum_ = 0
    for integer in array:
        sum_ += integer
    return sum_


# noinspection PyMethodMayBeStatic,PyPep8Naming, PyUnusedLocal
class Solution:

    # My solution to https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1
    # Note: len(A) is guaranteed to be equal to len(B)
    def check(self, A, B, N):
        frequencies = dict()
        for element in A:
            if element not in frequencies:
                frequencies[element] = 1
            else:
                frequencies[element] += 1
        for element in B:
            if element not in frequencies:
                return False
            else:
                frequencies[element] -= 1
        for key in frequencies:
            if frequencies[key] != 0:
                return False
        return True

    # My solution for https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1/
    # Function to find contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr, N):
        if arr and N == len(arr):
            maximum_sum = arr[0]
            current_maximum_sum = arr[0]
            for index in range(1, N):
                current_maximum_sum = max(arr[index], current_maximum_sum + arr[index])
                maximum_sum = max(current_maximum_sum, maximum_sum)
            return maximum_sum

    # My solution for https://practice.geeksforgeeks.org/problems/minimize-the-sum-of-product1525/1
    def minValue(self, a, b, n):
        a.sort(), b.sort()
        sum_ = 0
        for index, value in enumerate(a):
            sum_ += value * b[n - index - 1]
        return sum_

    # My solution for https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1
    def MissingNumber(self, array, n):
        valid_input = array is not None and len(array) + 1 == n
        if valid_input:
            expected_sum = int(n * (n + 1) / 2)
            actual_sum = 0
            for integer in array:
                actual_sum += integer
            return expected_sum - actual_sum
        return -1

    # My solution to https://practice.geeksforgeeks.org/problems/reverse-array-in-groups0255/1
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, N, K):

        for array_index in range(0, N, K):

            subgroup_first_index = array_index
            subgroup_last_index = min(N, array_index + K) - 1

            while subgroup_first_index < subgroup_last_index:
                temp = arr[subgroup_first_index]
                arr[subgroup_first_index] = arr[subgroup_last_index]
                arr[subgroup_last_index] = temp
                subgroup_first_index += 1
                subgroup_last_index -= 1

        return arr

    # https://practice.geeksforgeeks.org/problems/rotate-a-2d-array-without-using-extra-space1004/1/
    def rotateMatrix(self, arr, n):
        max_index = n - 1
        for row_index in range(max_index):
            for col_index in range(row_index, max_index - row_index):
                temp = arr[row_index][col_index]
                arr[row_index][col_index] = arr[col_index][max_index - row_index]
                arr[col_index][max_index - row_index] = arr[max_index - row_index][
                    max_index - col_index
                ]
                arr[max_index - row_index][max_index - col_index] = arr[
                    max_index - col_index
                ][row_index]
                arr[max_index - col_index][row_index] = temp
        return arr

    # My solution for https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1
    def search(self, A: list, l: int, h: int, key: int):
        # rename variables from problem for clarity and later reinitialization
        array = A
        left_index = l
        right_index = h

        if (
            not array
            or (left_index < 0 or right_index < 0)
            or (right_index < left_index)
        ):
            return -1

        def _find_pivot_index():
            nonlocal left_index, right_index
            while left_index < right_index:
                middle_index_ = int((left_index + right_index) / 2)
                if array[middle_index_] > array[right_index]:
                    left_index = middle_index_ + 1
                else:
                    right_index = middle_index_
            return left_index

        pivot_index = _find_pivot_index()

        # determine if key exists in subarray to left or right of pivot index and reset indices accordingly
        if array[pivot_index] <= key <= array[h]:
            left_index = pivot_index
            right_index = h
        else:
            left_index = l
            right_index = pivot_index

        # standard binary search within new bounds
        while left_index <= right_index:
            middle_index = int((left_index + right_index) / 2)
            middle_value = array[middle_index]
            if middle_value == key:
                return middle_index
            elif middle_value < key:
                left_index = middle_index + 1
            else:
                right_index = middle_index - 1

        return -1

    # My solution to https://practice.geeksforgeeks.org/problems/convert-array-into-zig-zag-fashion1638/1
    def zigZag(self, arr, n):

        valid_input = arr is not None and n == len(arr)
        if not valid_input:
            return None

        less_than = True

        for index in range(n - 1):
            if (
                less_than
                and arr[index] > arr[index + 1]
                or not less_than
                and arr[index] < arr[index + 1]
            ):
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
            less_than = not less_than

        return arr
