# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        head = ListNode(0)
        new = head
        while current1 and current2:
            if current1.val < current2.val:
                new.next = current1
                current1 = current1.next
            else:
                new.next = current2
                current2 = current2.next
            new = new.next
        new.next = current1 or current2
        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(4)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

a = Solution()
print(a.mergeTwoLists(head, head2))
