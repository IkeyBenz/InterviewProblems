# Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order** and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example:**
```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

---

### Clarifying Questions:
1. I am given the first node of each linked list?
2. Do I return the linked list I create, or just its first node?

### Assumptions:
1. Because the function's return type was declared as a ListNode, (in LeetCode at least)
I assume I'm suppose to just return the first node.
2. I'm assuming the type of ListNode.val is int

### Think out loud:
I'm thinking I might make a helper function called something like reversed_list_to_int, which will take a ListNode object, and return an integer. I'd use that function to convert my inputs into integers so that I can just add them, and then turn the output into a linked list.

The above idea is somewhat inefficient. I think that since the integers are stored in reversed order, its a good hint that we should just do basic math with them as we itterate. If we use a while loop that runs while the first node or the second node still has a next property, we'll be able to keep adding the nodes together until we're left with an answer.

### Solution:
```py
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
  # Create pointer to head:
  pointer_to_head = ListNode(None)

  curr = pointer_to_head
  carry = 0
  while l1 or l2:
    num1 = l1.val if l1 else 0
    num2 = l2.val if l2 else 0

    sum = num1 + num1 + carry
    carry = sum // 10
    curr = curr.next = ListNode(sum % 10)

    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None
  
  if carry > 0:
    curr.next = ListNode(carry)

  return head.next

```

### Thoughts:
I think that the manual addition solution is better than my original thought, becasue now the runtime is just O(n) where n is the longer integer between l1 and l2.