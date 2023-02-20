from turtle import st


class Solution:
    def nextsmallestelement(self,arr):
        stk=[]
        # ----> left 
        ln = len(arr)
        res=[ln]*ln
        for i in range(ln-1,-1,-1):
            if stk:
                while arr[stk[-1]]>=arr[i]:
                    stk.pop()
                    if not stk:
                        break
                if stk:
                    res[i]= stk[-1]
            stk.append(i)
        return res

a=Solution()
x= a.nextsmallestelement([3,1])
print(x)