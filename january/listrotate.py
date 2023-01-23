# Definition for singly-linked list.
class ListNode:
    def __init__(self, x,next= None):
        self.val = x
        self.next = next

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        head = A
        lst=[]
        c=0 
        while head:
            lst.append(head.val)
            head= head.next
        B=B%len(lst) # remove reduntent runs 
        
        head = A
        while head :
            head.val=lst[B-1]
            B+=1
            if B==len(lst):
                B=0
            head= head.next
        return A  
         
x= ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
a=Solution()
x= a.rotateRight(x,5)
while x:
    print(x.val)
    x=x.next