'''
https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        left, right, stack = "({[", ")}]", []
        for item in s:
            if item in left:
                stack.append(item)
            else:
                if not stack or left.find(stack.pop()) != right.find(item):
                    return False
        return not stack


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('()'))  # True
    print(s.isValid('()[]{}'))  # True
    print(s.isValid('(]'))  # False
    print(s.isValid('([)]'))  # False
    print(s.isValid('{[]}'))  # True
