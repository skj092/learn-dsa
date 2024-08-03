'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
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
        if index < len(root_list) and root_list[index] is not None:
            current.left = TreeNode(root_list[index])
            queue.append(current.left)
        index += 1
        # assign right
        if index < len(root_list) and root_list[index] is not None:
            current.right = TreeNode(root_list[index])
            queue.append(current.right)
        index += 1
    return root


def print_tree(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    print(result)


def diameter(root):
    res = 0

    def dfs(curr):
        if not curr:
            return 0

        left = dfs(curr.left)
        right = dfs(curr.right)

        nonlocal res
        res = max(res, left + right)
        return 1 + max(left, right)

    dfs(root)

    return res


if __name__ == "__main__":
    root = list(range(12))
    root = create_binary_tree(root)
    print_tree(root)
    print(diameter(root))
