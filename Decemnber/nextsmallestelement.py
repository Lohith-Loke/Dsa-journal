# NSE
# rightsmallestlelement
import re


class Solution:
    # @param A: List of integer
    # @return list of integer
    def leftsmallestlelement(self,A):
        res=[]
        stq=[]
        i=len(A)-1
        while i>-1:
            if stq:
                while stq[-1]>A[i]:
                    stq.pop()
                    if not stq:
                        break
                if stq:
                    res.append(stq[-1])
                else:
                    res.append(-1)
            else:
                res.append(-1)
            stq.append(A[i])
            i-=1
        res.reverse()
        return res
    def rightsmallestelement(slef,A):
        stq=[]
        res=[]
        i=0
        while i<len(A):
            if stq:
                while stq[-1]>A[i]:
                    stq.pop()
                    if not stq:# empty 
                        break
                if stq:
                    res.append(stq[-1])
                else:
                    res.append(-1)
            else:
                res.append(-1)
            stq.append(A[i])
            i+=1
        return res
# to left  
A=[2,3,5,6,3,2]
a=Solution()
x=a.leftsmallestlelement(A)
y=a.rightsmallestelement(A)

print(A)
print(x)
print(y)