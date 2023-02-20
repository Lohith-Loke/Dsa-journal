# kadane
# circular maxSumSubarray
# leetoode ok solution 
class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find max sum whithout circular kadane method 
        max_sum=A[0]
        sm=A[0]
        totsum=A[0]
        for i in range(1,len(A)):
            sm=max(sm+A[i],A[i])
            max_sum=max(max_sum,sm)
            totsum+=A[i]
        
        # get min sum subarray without circulation 
        min_sum=A[0]
        sm=A[0]
        for i in range(1,len(A)):
            sm=min(sm+A[i],A[i])
            min_sum=min(min_sum,sm)        
        x=max_sum
        if totsum-min_sum!=0:
            x=max(totsum-min_sum,max_sum)
        return x

A=[5,-3,5]
a=Solution()
x=a.maxSubArray(A)
print(x)