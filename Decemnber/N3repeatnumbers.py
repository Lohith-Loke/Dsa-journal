class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        # n/3 = x
        x=len(A)//3
        dk={}
        for i in A:
            if i in dk:
                dk[i]+=1
                if dk[i]>x:
                    return i 
            else:
                dk[i]=1
        return -1

A=[1,2,3,1,1]
s=Solution()
x=s.repeatedNumber(A)
print(x)