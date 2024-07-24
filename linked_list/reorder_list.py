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
        print(head.val)
        head = head.next


def create_linked_list(head_val):
    # create a linked list
    dummy = l1 = ListNode()
    for i in head_val:
        l1.next = ListNode(i)
        l1 = l1.next
    return dummy.next


def reorder_list(head):
    slow = head
    fast = head
    # Step 1: Go to the mid of list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step2: Reverse the second half
    second = slow.next
    prev = slow.next = None
    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp
    # Step3: Merge prev and head
    one = head
    two = prev

    while two:
        temp1, temp2 = one.next, two.next
        one.next = two
        two.next = temp1

        one = temp1
        two = temp2

    return head


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]
    # create a linked list
    l1 = create_linked_list(head)
    print_list(l1)

    print("=" * 30)
    l2 = reorder_list(l1)
    print_list(l2)
