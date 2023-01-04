class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        c=0
        while A!=0:
           q=A%2
           if q==1:
               c+=1
           A=A//2
        return c
a=Solution()
x=a.numSetBits(10)
print(x)