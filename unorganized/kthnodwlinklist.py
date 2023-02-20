# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, A, B):
        pass


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

a = Solution()
head = a.removeNthFromEnd(head1, 1)
while head != None:
    print(head.val,end=" -> ")
    head = head.next