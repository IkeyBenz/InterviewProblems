# Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution, and you may not use the same element twice.

**Example:**
```py
nums = [2, 7, 11, 15]
target = 9

twoSum(nums, target)
# Returns [0, 1], becasue nums[0] + nums[1] = 2 + 7 = 9
```

---

### Clarifying Questions:
1. Is the array of integers sorted?

### Assumptions:
1. Each input has exactly one solution
2. We should not assume that the integer array is sorted

### Think out loud:
Ok, so the naive solution would be to get every possible combination of sums
from the integer array, and then return the one that adds up to target. But that
would O(n^2) runtime and we could probably do better.

Rather than searching for two numbers that add up to target using a nested for loop,
we can use one loop to itterate over each number, and then store the difference between
that number and the target in a hashtable. This way, we will have a hashtable of complements
and their indices to search from within the loop. Since searching through a hashtable is O(1)
runtime on average, at worst our algorithm will run in O(n) time.

### Solution:
```py
def twoSum(nums: [int], target: int) -> [int]:
  compliment_index = {}

  for ind, num in enumerate(nums):
    compliment = target - num

    if compliment in compliments:
      return [ind, compliment_index[compliment]]

    compliment_index[compliment] = ind
```

### Thoughts:
This type of problem requires that at least every number in the input gets checked,
so I don't think we could do better than O(n) runtime. This algo also takes O(n) space
for the hashtable, but I wouldn't remove that becasue it's what allows us to not have O(n^2)
runtime.