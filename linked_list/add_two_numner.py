"""
Problem Statement:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(head.val, end=' ')
        head = head.next


def add_list(head1, head2):
    temp = dummy = ListNode()
    carry = 0
    while head1 or head2 or carry:
        val1 = head1.val if head1 else 0
        val2 = head2.val if head2 else 0

        add_values = val1 + val2 + carry
        s = add_values % 10
        carry = add_values // 10
        dummy.next = ListNode(s)
        dummy = dummy.next

        head1 = head1.next if head1 else None
        head2 = head2.next if head2 else None
    return temp.next


if __name__ == "__main__":
    l1 = temp1 = ListNode()
    l2 = temp2 = ListNode()

    vals1 = [2, 4, 3]
    vals2 = [5, 6, 4]

    for v1, v2 in zip(vals1, vals2):
        n1, n2 = ListNode(val=v1), ListNode(val=v2)
        temp1.next = n1
        temp2.next = n2
        temp1 = temp1.next
        temp2 = temp2.next

    print_list(l1.next)
    print("\n ============")
    print_list(l2.next)
    print("\n ============")

    a = add_list(l1.next, l2.next)
    print_list(a)
