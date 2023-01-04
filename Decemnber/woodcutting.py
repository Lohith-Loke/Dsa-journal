class Solution:

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort(reverse=True)# 54321
        # print(A)
        h=A[0] # h= max(A)
        sm=0
        while sm <B:
            h=h-1
            j=0
            sm=0
            while A[j] > h:
                sm+=A[j]-h
                j+=1
        #sm  > == B 
        return h

s=Solution()
x=s.solve(A=[4, 42, 40, 26, 46],B=20)
print(x)