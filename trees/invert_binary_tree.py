'''
Problem Statement: Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(root_list):
    if not root_list:
        return None

    root = TreeNode(root_list[0])
    queue = [root]

    index = 1
    while index < len(root_list):
        current = queue.pop(0)

        # assign left
        if index < len(root_list):
            current.left = TreeNode(root_list[index])
            queue.append(current.left)
            index += 1

        # assign right
        if index < len(root_list):
            current.right = TreeNode(root_list[index])
            index += 1

    return root


def print_tree(root):
    if not root:
        return []

    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print(result)


def invert_binary_tree(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root


if __name__ == "__main__":
    root_list = [4, 2, 7, 1, 3, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17]

    root = create_binary_tree(root_list)
    print_tree(root)
    inv = invert_binary_tree(root)
    print_tree(inv)
