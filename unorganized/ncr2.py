from math import gcd


def Ncr(n, r):
    p = 1
    k = 1
    if n < r:
        raise ValueError(" arg 1:n canot be greater than arg2:r ")
    if (n-r < r):
        r = n-r
    if r == 0:
        return p
    while (r):
        p *= n
        k *= r
        m = gcd(p, k)
        p //= m
        k //= m
        n -= 1
        r -= 1
    return p


n = 10
r = 10
res = Ncr(n, r)
print(res)
