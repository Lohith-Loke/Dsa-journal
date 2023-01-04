from math import sqrt


class Solution:
    ans=0 
    def binserch(self,A,high,low):
        
        if low>high:
            # we dont hope to reach here 
            return self.ans
        mid = (low+high)//2 
        
        if mid * mid > A :
            # sqre(mid) > A :: sqrt(A) is b/w  low mid-1
            return self.binserch(A, mid-1 ,low)
            
        
        if mid * mid < A :
            # sqre(mid ) < A :: sqrt(A) is b/w mid+1 high
            self.ans = mid
            return self.binserch(A,high,mid+1)
            
        if mid * mid == A :
            return mid 

A=1
a=Solution()

x=a.binserch(A,A//2+1,1)
print(x)
print(int(sqrt(A)))