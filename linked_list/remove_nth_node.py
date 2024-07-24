'''
Problem Statement: Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]

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


def remove_nth(head, n):
    r = head
    dummy = l = ListNode(next=head)
    # step 1: place right pointer to the nth value from start
    while n:
        r = r.next
        n -= 1
    # Step 2: Slide till right goes on last node
    while r:
        l = l.next
        r = r.next
    # Step3: Update the pointer
    l.next = l.next.next
    return dummy.next


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]
    n = 2
    head = [1]
    n = 1

    # create a linked list
    l1 = create_linked_list(head)
    print_list(l1)
    print("=" * 30)

    # remove nth from the last
    l2 = remove_nth(l1, n)
    print_list(l2)
