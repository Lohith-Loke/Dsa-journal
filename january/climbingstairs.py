class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        first=1
        second=1
        for i in range(2 , n+1):
            nxt= first+ second
            first= second
            second= nxt
        return nxt
n=2
a=Solution()
x=a.climbStairs(38)
print(x)