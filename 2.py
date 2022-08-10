# Definition for singly-linked list.
# pallendrome link list with o(1) space o(n) time 

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, ptr):
        prev = 0
        while ptr:
            next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # using 2 pointer and node reversal
        slow = head
        fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # slow is in middle
        # reverse pointer direction
        revhead = self.reverse(slow)

        while head and revhead:
            if revhead.val != head.val:
                return False
            revhead = revhead.next
            head = head.next
        return True
        # Using a list
        # l = []
        # current = head
        # while current:
        #     l.append(current.val)
        #     current = current.next
        # # l conntains list
        # start = 0
        # end = len(l)-1
        # while start < end:
        #     if l[start] != l[end]:
        #         return False
        #     start = start+1
        #     end = end-1
        # return True


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)


a = Solution()
if(a.isPalindrome(head)):
    print("true")
else:
    print("false")
