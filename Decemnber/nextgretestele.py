# using stack 
class Solution:
    # @param list of int 
    # @return list of int 
    def nextgreatestelement(self,A):
        res=[]
        stq=[]
        i= len(A)-1
        while i>-1: # o(N)
            if stq:
                # while stq.last > A[i]
                while stq[-1]<A[i]:
                    if stq:
                        stq.pop()
                    else:
                        break
                if stq:
                    res.append(stq[-1])
                else:
                    res.append(-1)
            else:
                # stq is empty
                res.append(-1)
            
            stq.append(A[i])
            i-=1
        res.reverse() # O(N)
        return res

A=[1,3,2,4]
a=Solution()
x=a.nextgreatestelement(A)
print(A)
print(x)