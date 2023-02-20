#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from operator import le


class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        tot=len(A)+len(B)
        half=tot//2 
        # we need to get half No of elements in coreect order 
        if len(A)<len(B):
            A,B=B,A
        # A is always longest of array 
        l=0 
        ar=half//2+1
        br=half//2-1

        if len(A)<ar:
            if A[ar]<B[br]:
                


         

A=[1,2,3,4,7]
B=[3,4,5,7]
a=Solution()
x=a.findMedianSortedArrays(A,B)
print(x)
# @lc code=end

