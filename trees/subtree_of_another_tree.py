'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,None,None,None,None,0], subRoot = [4,1,2]
Output: false

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


def is_subtree(p, q):
    if not q:
        return True
    if not p:
        return False
    if is_same(p, q):
        return True

    return is_subtree(p.left, q) or is_subtree(p.right, q)


def is_same(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return is_same(p.left, q.left) and is_same(p.right, q.right)


if __name__ == "__main__":
    root = [3, 4, 5, 1, 2]
    subRoot = [4, 1, 2]
    #root = [3, 4, 5, 1, 2, None, None, None, None, 0]
    #subRoot = [4, 1, 2]
    root = create_binary_tree(root)
    subRoot = create_binary_tree(subRoot)
    print_tree(root)
    print_tree(subRoot)
    print(is_same(root, subRoot))
    print(is_subtree(root, subRoot))
