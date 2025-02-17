def two_sum(list_, target_sum):
    discovered = set()
    result = set()
    for element in list_:
        compliment = target_sum - element
        if compliment in discovered:
            ordered_pair = (min(element, compliment), max(element, compliment))
            result.add(ordered_pair)
        discovered.add(element)
    return result


class Solution:

    # My solution to https://practice.geeksforgeeks.org/problems/find-all-pairs-whose-sum-is-x5808/1
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def allPairs(self, A, B, N, M, X):
        A.sort()
        set_b = set(B)
        result = []
        for u in A:
            v = X - u
            if v in set_b:
                result.append((u, v))
        return result
    
    # My solution to https://leetcode.com/problems/two-sum
    def twoSum(self, nums, target):
        discovered = dict()
        result = list()
        for index, num in enumerate(nums):
            complement = target - num
            if complement in discovered:
                return [discovered[complement], index]
            else:
                discovered[num] = index
        return result
