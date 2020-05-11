from rotate_linked_list import LinkedList


def middle_from_linked_list(lst: LinkedList):
    '''
        Given a singly linked list, finds the middle value in the list
    '''
    middle = len(lst) // 2
    for index, val in enumerate(lst):
        if index == middle:
            return val


if __name__ == '__main__':
    # 1. Find middle value in linked list of odd length
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(middle_from_linked_list(lst))  # Prints 5

    # 4. Rotate a list by k nodes
    lst = LinkedList(['A', 'B', 'C', 'D', 'E', 'F'])
    lst.rotate(4)
    print(lst)  # Prints "E -> F -> A -> B -> C -> D"
