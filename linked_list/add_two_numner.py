'''
Problem Statement: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
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


def add_two(l1, l2):
    dummy = n = ListNode()
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        add = val1 + val2 + carry
        sum = add % 10
        carry = add // 10
        n.next = ListNode(sum)

        n = n.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next


if __name__ == "__main__":
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    # create a linked list
    l1 = create_linked_list(l1)
    l2 = create_linked_list(l2)

    # Print l1 and l2
    print_list(l1)
    print("=" * 30)
    print_list(l2)
    print("=" * 30)

    # add l1 and l2
    l3 = add_two(l1, l2)
    print_list(l3)
