class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        i=0
        j=0
        ans=0
        cursum=0
        while i<len(A):
            cursum+=A[i]
            while cursum>=B:
                cursum-=A[j]
                j+=1
            ans+=(i-j+1)
            i+=1
        return ans
A = [ 8, 5, 1, 10, 5, 9, 9, 3, 5, 6, 6, 2, 8, 2, 2, 6, 3, 8, 7, 2, 5, 3, 4, 3, 3, 2, 7, 9, 6, 8, 7, 2, 9, 10, 3, 8, 10, 6, 5, 4, 2, 3, 4, 4, 5, 2, 2, 4, 9, 8, 5 ]

B = 32
ans=4
a=Solution()
x=a.solve(A,B)
print(x)