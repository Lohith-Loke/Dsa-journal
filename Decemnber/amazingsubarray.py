class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        dk={}
        st="aeiouAEIOU"
        for i in st:
            dk[i]=0;
        ln=len(A)
        tot=0 
        for i in range(ln):
            if A[i] in dk:
                # we dont need to find it we need to calculate all substring 
                tot+=ln-i
        return tot % 10003

A="ABEC"
s=Solution()
x=s.solve(A)
print(x)