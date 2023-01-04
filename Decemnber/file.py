class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)==0 or len(A)==1:
            return len(A)
        j=0
        ln=len(A)-1
        for i in range(ln):
            if A[i]!=A[i+1] and A[i]==A[i-1]:
                A[j]=A[i]
                j+=1
                A[j]=A[i]
                j+=1
            else:
                A[j]=A[i]
                j+=1    
        # look at
        # print(j,A[j])
        if A[ln] == A[ln-1]: # 4 
            A[j]=A[ln]
            j+=1    # A[5] 5 
            A[j]=A[ln-1]
            j+=1
        else:
            A[j]=A[ln]
            j+=1

        print(A[:j])
        return j
A=[ 0 ,0 ,0 ,1 ,1, 2, 2 ,3]
a=Solution()
x=a.removeDuplicates(A)
print(x)