'''
Problem Statement: Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(head.val, end=' ')
        head = head.next


def remove_nth_node(head, n):
    # set the position of right
    l = dummy = ListNode()
    l.next = head
    r = head

    while n:
        r = r.next
        n -= 1

    # slide left and right to the end of the list
    while r.next:
        l = l.next
        r = r.next

    # delete the node
    l.next = l.next.next
    return dummy.next


if __name__ == "__main__":
    l1 = temp1 = ListNode()

    vals1 = [1, 2, 3, 4, 5]
    n = 2

    for v1 in vals1:
        n1 = ListNode(val=v1)
        temp1.next = n1
        temp1 = temp1.next

    print_list(l1.next)
    print("\n ============")

    nth = remove_nth_node(l1.next, n)
    print_list(nth)
