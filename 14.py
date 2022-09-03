# compute total number of ways to reach nth stairs
class Solution:
    # @param n : number of stairs 
    # @return an integer
    def solve(self, n):
        one,two=1,1
        l=[]
        l.append(1)
        l.append(1)
        for i in range(1,n):
            temp=one
            one=two+one
            two=temp
            l.append(one)
        return one

a = Solution()
# a.solve(n=5)
z=a.solve(n=4)
print(z)