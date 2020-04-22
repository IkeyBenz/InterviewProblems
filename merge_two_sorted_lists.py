'''
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        out = f'{self.val}'
        curr = self
        while curr.next:
            out += f' -> {curr.next.val}'
            curr = curr.next
        return f'HEAD -> {out} -> None'


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


def make_linked(lst: list) -> ListNode:
    head = ListNode(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


if __name__ == '__main__':
    s = Solution()
    l1 = make_linked([1, 2, 4])
    l2 = make_linked([1, 3, 4])
    print(s.mergeTwoLists(l1, l2))
