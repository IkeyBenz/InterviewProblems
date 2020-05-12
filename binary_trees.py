from math import fabs


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def has_children(self):
        return self.left or self.right

    def depth(self):
        left_depth = 0 if not self.left else self.left.depth()
        right_depth = 0 if not self.right else self.right.depth()
        return 1 + max(left_depth, right_depth)


def reverse_binary_tree(node: BinaryTreeNode):
    node.right, node.left = node.left, node.right
    node.left and reverse_binary_tree(node.left)
    node.right and reverse_binary_tree(node.right)


def is_super_balanced(node: BinaryTreeNode):
    left_depth = 0 if not node.left else node.left.depth()
    right_depth = 0 if not node.right else node.right.depth()

    return all([
        fabs(left_depth - right_depth) <= 1,
        not node.left or is_super_balanced(node.left),
        not node.right or is_super_balanced(node.right)
    ])


def in_order_traversal(node: BinaryTreeNode):
    ordered = []
    if node.left:
        ordered.extend(in_order_traversal(node.left))
    ordered.append(node.data)
    if node.right:
        ordered.extend(in_order_traversal(node.right))
    return ordered


if __name__ == '__main__':

    # Testing is_super_balanced
    head = BinaryTreeNode(50)
    head.left = BinaryTreeNode(25)
    head.left.left = BinaryTreeNode(12.5)
    head.left.right = BinaryTreeNode(37.5)
    print(is_super_balanced(head))  # Correctly prints False
    head.right = BinaryTreeNode(75)
    head.right.right = BinaryTreeNode(87.5)
    head.right.left = BinaryTreeNode(62.5)
    print(is_super_balanced(head))  # Correctly prints True

    # Testing reverse_binary_tree
    print(in_order_traversal(head))
    reverse_binary_tree(head)
    print(in_order_traversal(head))  # This one is reversed
