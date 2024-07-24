'''
Problem Statement: You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(head.val)
        head = head.next


def create_linked_list(head_val):
    # create a linked list
    dummy = l1 = ListNode()
    for i in head_val:
        l1.next = ListNode(i)
        l1 = l1.next
    return dummy.next


def merge(l1, l2):
    dummy = node = ListNode()

    while l1 and l2:
        if l1.val < l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next
    node.next = l1 or l2
    return dummy.next


if __name__ == "__main__":
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]

    # create a linked list
    l1 = create_linked_list(list1)
    l2 = create_linked_list(list2)
    print_list(l1)
    print("=" * 30)
    print_list(l2)

    print("=" * 30)
    l3 = merge(l1, l2)
    print_list(l3)
