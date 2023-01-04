class Solution:
    # @param A : string
     # @return an long
    def countSalutes(self, A):
        i = 0
        ln=len(A)
        while i <ln:
            if A[i]==">":
                break
            i+=1
        # i is first > in A
        init=0
        mul=1
        zerocount=0
        # ><<><
        while i<ln-1:
            i +=1
            if A[i]=="<":
                zerocount+=1 
            else :
            #   A[i] == >   
                mul+=1
                init+=zerocount # 
        ans = (zerocount*mul)-init 
        return ans

A='<>'
a=Solution()
x=a.countSalutes(A)
print(x)