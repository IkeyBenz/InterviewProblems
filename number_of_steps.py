'''
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

Given a non-negative integer num, return the number of steps to reduce it to zero.
If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
'''


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num != 0:
            steps += 1
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
        return steps


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSteps(14))  # 6
