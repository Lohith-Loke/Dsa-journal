# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head= None
        if list1:
            if list2:
                if list1.val <list2.val:
                    head = list1
                    list1=list1.next
                else:
                    head= list2
                    list2=list2.next
            else:
                # list 2 is null
                head=None
        else:
            if list2:
                head=list2
                list2=list2.next
            else:
                head=None
        root = head

        while True:
            if list1:
                if list2:
                    if list1.val <list2.val:
                        head.next = list1
                        head= head.next
                        list1=list1.next
                    else:
                        head.next = list2
                        head= head.next
                        list2=list2.next

                else:
                # list 2 is null
                # list 1 and list 2 are empty
                    head.next=list1
                    head=head.next
                    list1=list1.next
            else:

                if list2:
                    head.next=list2
                    head=head.next
                    list2=list2.next
                else:
                    # both are null
                    break
        return root
x=None
y=ListNode(2,ListNode(5,ListNode(6)))
a=Solution()
z=a.mergeTwoLists(x,y)
while z:
    print(z.val)
    z=z.next
