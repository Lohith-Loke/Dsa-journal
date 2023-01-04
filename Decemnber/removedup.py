class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        dk={}
        for i in A:
            if i not in dk:
                dk[i]=None
        uniq=list(dk.keys())
        uniq.sort()
        for i in range(len(uniq)):
            A[i]=uniq[i]

        return len(uniq) 

A=[0]
a=Solution()
a.removeDuplicates(A)  