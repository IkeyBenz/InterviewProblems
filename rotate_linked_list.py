'''
Rotate a given linked list counter-clockwise by k nodes, where k is a given integer.


Clarifying Questions:
 - Clarify what counter-clockwise entails. Move back to front or opposite?
 - Is it a singly linked, or doubly linked list?

Resonable Assumptions:
 - It is a singly linked list
 - K is less than the number of nodes in the list

Ways to simplify:
 - Quit

Ways to approach:
 - Make LinkedList class with rotate instance method

Psuedo code:
Loop K times:
    Remove first element from list
    Append it to end of list
'''


class LinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self, items):
        self.head = LinkedList.Node()
        self.tail = self.head
        self.length = 0

        for item in items:
            self.append(item)

    def __str__(self):
        return ' -> '.join(map(str, list(self)))

    def __len__(self):
        return self.length

    def __iter__(self):
        node = self.head
        while node.next is not None:  # Skip head
            yield node.next.data
            node = node.next

    def append(self, item):
        self.tail.next = LinkedList.Node(item)
        self.tail = self.tail.next
        self.length += 1

    def remove_first_occurance_of(self, item):
        node = self.head
        while node.next is not None:
            if node.next.data == item:
                node.next = node.next.next
                self.length -= 1
                break

    def rotate(self, k):
        k %= len(self)  # Edge case of unneccesary rotations
        for _ in range(k):
            first_item = self.head.next.data
            self.remove_first_occurance_of(first_item)
            self.append(first_item)


if __name__ == '__main__':
    l = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(l)
    l.rotate(10)
    print(l)
