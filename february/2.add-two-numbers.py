#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1=0
        num2=0
        i=0
        while l1:
            num1=num1+l1.val*(10**i)
            l1=l1.next
            i+=1
        i=0
        while l2:
            num2=num2+l2.val*(10**i)
            l2=l2.next
            i+=1
        
        sol=sum([num1,num2])
        root=head=ListNode(sol%10)
        sol=sol//10
        
        while sol!=0:
            q=sol%10
            head.next=ListNode(q) 
            sol=sol//10
            head=head.next
        
        return root
# @lc code=end
def arrtolist(arr):
    head=ListNode(arr[0])
    cur=head
    for i in range(1,len(arr)):
        cur.next=ListNode(arr[i])
        cur=cur.next
    return head

a=Solution()
a.addTwoNumbers(arrtolist([2,4,3]),arrtolist([5,6,4]))
