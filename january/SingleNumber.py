class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        A.sort()
        i=1
        while i<len(A):
            if A[i]==A[i-1]:
                if i+2>=len(A):
                    # near end of array 
                    return A[i+1]   
                i+=2
            else:
                return A[i-1]

A=[1, 2,3, 3, 1]
a=Solution()
x=a.singleNumber(A)
print(x)