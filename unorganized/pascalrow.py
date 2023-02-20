from math import gcd


class Solution:
    def Ncr(self, n, r):
        p = k = 1
        if (n-r < r):
            r = n-r
        if r == 0:
            return p
        while(r):
            p *= n
            k *= r
            m = gcd(p, k)
            p //= m
            k //= m
            n -= 1
            r -= 1
        return p

    def pascalrow(self, n):
        res = []
        res2 = []
        l = int(n//2)+1
        for i in range(l):
            sol = self.Ncr(n, i)
            res.append(sol)
            res2.append(sol)
        res2.reverse()
        if n % 2 != 0:
            return res+res2
        return res+res2[1:]


a = Solution()
print(a.pascalrow(3))