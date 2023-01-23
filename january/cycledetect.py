# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dk={}
        key=None
        if head:
            key=head
            head=head.next
        c=0
        while head:
            c+=1
            if c==1000:
                break 

            if key in dk:
                if dk[key.val]==head.val:
                    return key
                else:
                    break
            else:
                # possible duplication 
                dk[key]=head
                key=head
                head=head.next

                
z=ListNode(2,ListNode(5,ListNode(6,ListNode(7,ListNode(5,ListNode(6,ListNode(7)))))))

a=Solution()
y=a.detectCycle(z)

while y:
    print(y.val)
    y=y.next
