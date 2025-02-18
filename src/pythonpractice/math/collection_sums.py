from pythonpractice.datastructures.list.linkedlist import ListNode

# Define ListNode locally to resolve the error
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

    # seems like O(3n), probably could make O(n)
    def addTwoNumbers(self, lst1, lst2):

        def build_reversed_num(lst_node):
            multiplier = 1
            result = 0
            while lst_node:
                num = lst_node.val * multiplier
                result += num
                multiplier *= 10
                lst_node = lst_node.next
            return result

        def build_reversed_list(num):
            current = head = ListNode()
            while num > 0:
                current.val = num % 10
                num //= 10
                if num > 0:
                    current.next = ListNode()
                    current = current.next
            return head

        reversed_sum = build_reversed_num(lst1) + build_reversed_num(lst2)
        return build_reversed_list(reversed_sum)

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
