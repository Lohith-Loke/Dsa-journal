#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start

class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # solution 
        tot=len(A)+len(B)
        half=tot//2
        if len(B)<len(A):
            # make B the bigge array  
            A,B=B,A
        # left pointer right pointer 
        l,r=0,len(A)-1
        while True:
            # get middle of left and right
            ai=(l+r)//2

            j=half- ai- 2 # array index issue 
            Aleft=A[ai] if ai >= 0 else float("-infinity")
            Aright=A[ai+1] if (ai+1) < len(A) else float("infinity")
            Bleft=B[j] if (j+1) >= 0 else float("-infinity")
            Bright=B[j+1] if (j+1) < len(B) else float("infinity")
            
            if Aleft<=Bright and Bleft<=Aright:
                if tot%2==0:
                    return min(Aright,Bright)
                return (max(Aleft,Bleft)+min(Aleft,Bright))/2
            elif Aleft >Bright:
                r=ai-1
            else:
                l=ai+1
        
# @lc code=end
A=[1,3]
B=[2]
a=Solution()
x=a.findMedianSortedArrays(A,B)
print(x)
