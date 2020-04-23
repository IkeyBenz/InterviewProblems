'''
https://leetcode.com/problems/power-of-two/

Given an integer, write a function to determine if it is a power of two.
'''


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return any(n == 2**i for i in range(32))


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(1))  # True
    print(s.isPowerOfTwo(16))  # True
    print(s.isPowerOfTwo(218))  # False
