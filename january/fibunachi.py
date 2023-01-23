class Solution:
    def fib(self,n ):
        if n==0:
            return 0 
        if n==1:
            return 1 

        else:
            x=self.fib(n-1)+ self.fib(n-2)
            return x 
n= 10
a=Solution()
x= a.fib(n)
print(x) 