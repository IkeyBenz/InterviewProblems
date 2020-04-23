'''
https://leetcode.com/problems/search-insert-position/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''


class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))  # 2
    print(s.searchInsert([1, 3, 5, 6], 2))  # 1
    print(s.searchInsert([1, 3, 5, 6], 7))  # 4
    print(s.searchInsert([1, 3, 5, 6], 0))  # 0
