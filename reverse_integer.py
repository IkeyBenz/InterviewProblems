'''
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''


class Solution:
    def reverse(self, x) -> int:
        if x < 0:
            val = -int(str(x)[::-1][:-1])
        else:
            val = int(str(x)[::-1])

        if not -2**31 < val < 2**31:
            return 0

        return val


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(12345))  # 54321
    print(s.reverse(-12345))  # -54321
    print(s.reverse(1563847412))  # 0
