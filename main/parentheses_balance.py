# My solution for https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1
class Solution:

    # noinspection PyMethodMayBeStatic,SpellCheckingInspection
    def ispar(self, x):
        stack = []
        for character in x:
            if character in "{[(":
                stack.append(character)
            if character in "}])":
                if not stack:
                    return False
                next_stack_character = stack.pop()
                if character == '}' and next_stack_character != '{' or \
                        character == ']' and next_stack_character != '[' or \
                        character == ')' and next_stack_character != '(':
                    return False
        return not stack
