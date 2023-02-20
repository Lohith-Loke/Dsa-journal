
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        # if no intersection return null
        # dont modify the data
        # run time o(n)  space o(1)
        curA = A
        curB = B
        x = 0
        prv = None
        sol = None
        while True:

            if curA.val == curB.val:
                sol = curA
                while True:
                    if curA.val != curB.val:
                        x = -1
                        break
                    curA = curA.next
                    curB = curB.next
                    if curA == None and curB == None:
                        x=0
                        break

                if x == 0:
                    return sol
            if curA == None or curB == None:
                break
            curA = curA.next
            curB = curB.next
        return


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(5)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

a = Solution()
head = a.getIntersectionNode(head, head1)
while head != None:
    print(head.val)

    head = head.next
