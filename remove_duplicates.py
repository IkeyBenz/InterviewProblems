'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''


class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        idx = 1
        while idx < len(nums):
            if nums[idx - 1] == nums[idx]:
                nums.pop(idx)
            else:
                idx += 1
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1, 1, 2]))  # 2
