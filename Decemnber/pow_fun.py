class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n,d):
      # (ab % m)=((a%m)(b%m)) % m
      # (a * a * a ) %m =  ((a %m )(a%m)(a%m) )%m 
      
        res=1
        while n>0:
          print(n)
          if n%2 ==0:
            # (x%m * x%m )%m 
            x= (x%d * x%d)%d
            n=n//2
          else:
            #  (res%m * x%m )%m
            res= ((res%d) * (x%d))%d
            n=n-1
            
        return res


''''
A : 213
B : 231
C : 1

71045970
41535484
64735492
'''

A = 71045970
B = 41535484
C = 64735492
a=Solution()
x=a.pow(A,B,C)
# y=a.pow2(A,B)
print(x)
# print(y)
print(pow(A,B))
