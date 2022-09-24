
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        current = A
        c = B
        prv = None
        len = 0
        while current:
            len += 1
            c -= 1
            if c == 0:
                nextptr = current.next
                if current.next == None:
                    # lenth is acurate
                    pass
                else:
                    len += 1
                c = -1
                break
            prv = current
            current = current.next

        if c != -1 or len <= B:
            # reomve first element
            return A.next
        current = A
        while nextptr != None:
            prv = current
            current = current.next
            nextptr = nextptr.next

        prv.next = current.next
        return A


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
# head1.next.next.next.next.next = ListNode(85)

# 67 -> 27 -> 64 -> 10 -> 4 -> 85

a = Solution()
head = a.removeNthFromEnd(head1, 2)
while head != None:
    print(head.val)

    head = head.next
