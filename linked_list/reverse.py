'''
Problem Statemen: Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]
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


def reverse_list(head):
    curr = head
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


if __name__ == "__main__":
    head_val = [1, 2]
    head_val = [1, 2, 3, 4, 5]

    # create a linked list
    l1 = create_linked_list(head_val)
    print_list(l1)

    print("=" * 30)

    # reverse the linked list
    reversed = reverse_list(l1)
    print_list(reversed)
