# My solution for https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1
class Solution:

    # noinspection PyMethodMayBeStatic,SpellCheckingInspection
    def ispar(self, x):
        stack = []
        for character in x:
            if character in "{[(":
                stack.append(character)
            if character == '}':
                if not (stack and (stack.pop() == '{')):
                    return False
            if character == ']':
                if not (stack and (stack.pop() == '[')):
                    return False
            if character == ')':
                if not (stack and (stack.pop() == '(')):
                    return False
        return not stack
