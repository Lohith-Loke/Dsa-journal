# maxSumSubarray
class Solution(object):
    def maxSubArray(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=A[0]
        best=[]
        sm=0
        for i in range(0,len(A)):
            sm=max(0,sm+A[i],A[i])
            ans=max(ans,sm)
        return ans
A=[-2,1,-3,4,-1,2,1,-5,4]
a=Solution()
x=a.maxSubArray(A)
print(x)