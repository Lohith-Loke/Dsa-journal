class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        # a XOR b =a ^ b
        # a ^ b = (a OR b) AND (NOT (a AND b)) 
        A.sort()
        mx=1000000000
        for i in range(1,len(A)):
            mx=min(mx, A[i]^A[i-1] )
        return mx
A = [0, 2]
a=Solution()
x=a.findMinXor(A)
print(x)