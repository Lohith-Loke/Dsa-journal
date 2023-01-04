'''
I - 1 
V - 5 
X - 10 
L - 50 
C - 100
D - 500
M - 1000
'''


class Solution:
    def romantoint(self,A):
        dk={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        if A in dk:
            return dk[A]
        num=[]
        prv=10000
        for i in A:
            num.append(dk[i])
            
        # print(num)
        sm=0
        for i in range(len(num)):
            if prv<num[i]:
                sm=sm+num[i]-(num[i-1]*2)
                continue
            sm+=num[i]
            prv=num[i]
        return sm

A=""
a=Solution()
x=a.romantoint(A)
print(x)

