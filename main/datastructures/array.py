class Solution:

    # My solution to https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1
    # Note: len(A) is guaranteed to be equal to len(B)
    # noinspection PyMethodMayBeStatic,PyPep8Naming
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
        for element in frequencies:
            if frequencies[element] != 0:
                return False
        return True
