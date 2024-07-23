'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(head.val, end=' ')
        head = head.next


def re_order(head):
    # get the half
    s, f = head, head
    while f.next:
        s = s.next
        f = f.next.next
    # rotate 2nd half
    second = s.next
    prev = None
    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    # Join
    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1

        first = temp1
        second = temp2

    print_list(head)
    return head


if __name__ == "__main__":
    l1 = temp1 = ListNode()

    vals1 = [1, 2, 3, 4, 5]

    for v1 in vals1:
        n1 = ListNode(val=v1)
        temp1.next = n1
        temp1 = temp1.next

    print_list(l1.next)
    print("\n ============")
    s = re_order(l1.next)
