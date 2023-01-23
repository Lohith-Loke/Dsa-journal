class Solution(object):
    def subarraySum(self, A, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sm=0
        res=0
        rem=0
        dk={}
        for i in range(len(A)):
            sm=sm+A[i]
            if sm==k:
                res+=1
            rem= sm-k
            if rem in dk:
                res=res+dk[rem]
            if sm in dk:
                dk[sm]+=1
            else:
                dk[sm]=1
        return res
a=Solution()
x=a.subarraySum([1,1,1],2)
print(x)