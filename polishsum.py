from collections import deque

class Solution:
    def doop(self,a,b,op):
        a=int(a)
        b=int(b)
        if op==1:
            return a+b
        if op==2:
            return b-a
        if op==3:
            return a*b
        if op==4:
            return int(b/a)
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        # print(A)            
        l=deque()
        i =0
        d={'+':1, '-':2, '*':3, '/':4}
        # print('/' in d)
        while True:
            if i >len(A)-1:
                break
            if A[i] in d :
                # print("oop")
                # do operation 
                print(l,A[i])
                a=l.pop()
                # print(l)
                b=l.pop()
                c=self.doop(a,b,d[A[i]])
                print("sol=",c)
                l.append(c)
                i+=1
            else:
                l.append(A[i])
                # print(A[i])
                i+=1
                
        return l.popleft()
a=Solution()
x=a.evalRPN([ "4", "13", "5", "/", "+" ])
print(x)