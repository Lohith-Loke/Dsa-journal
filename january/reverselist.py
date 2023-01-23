# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # iterartive way 
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prv = None
        while head:
            nxt= head.next
            head.next = prv 
            prv = head
            head= nxt
        return prv 


    def revlthlp(self,head,root=None):
        if not head.next:
            # 5-> None
            root = head
            return head,root  # exit recursion 
        else:
            # there is next element 
            nxt,root=self.revlthlp(head.next)
            head.next=None
            nxt.next=head
            return head,root

    def reverseListrec(self, head,root=None):
        _,root=self.revlthlp(head)
        return root

x=None

z=ListNode(2,ListNode(5,ListNode(6,ListNode(7,ListNode(10)))))
a=Solution()
z=a.reverseList(z)
while z:
    print(z.val)
    z=z.next
