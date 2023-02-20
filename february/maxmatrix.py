# https://practice.geeksforgeeks.org/problems/maximum-sum-rectangle2948/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab
#User function Template for python3

#User function Template for python3


class Solution:
    def maximumSumRectangle(self,R,C,M):
        #code here
        _mxsum=-10000000000
        for cbegin in range(C):
            cend=cbegin
            sm=[0]*R
            while cend<C:
                for row in range(R):
                    sm[row] +=M[row][cend]             
                _mxsum=max(_mxsum,self.maxSubArray(sm))
                cend+=1
        return _mxsum
        
    # kadane algo 
    def maxSubArray(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=A[0]
        sm=0
        for i in range(0,len(A)):
            sm=max(sm+A[i],A[i])
            ans=max(ans,sm)
        return ans
R=4
C=5
M=[
[1,2,-1,-4,-20],
[-8,-3,4,2,1],
[3,8,10,1,3],
[-4,-1,1,7,-6]
]
a=Solution()
s=a.maximumSumRectangle(R,C,M)
print(s)