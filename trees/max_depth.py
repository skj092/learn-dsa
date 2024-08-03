'''
Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
'''

from collections import deque


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


def max_depth(root):
    if not root:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


def max_depth(root):
    if not root:
        return 0

    q = deque([root])
    level = 0
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        level += 1
    return level


def max_depth(root):
    if not root:
        return 0

    q = [[root, 1]]
    res = 0
    while q:
        node, depth = q.pop()
        if node:
            res = max(res, depth)
            q.append([node.left, depth + 1])
            q.append([node.right, depth + 1])
    return res


if __name__ == "__main__":
    root = [3, 9, 20, None, None, 15, 7]

    root = create_binary_tree(root)
    print_tree(root)
    print(max_depth(root))
