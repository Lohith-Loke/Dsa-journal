
def gcd(A, B):
    if A < B:
        temp = A
        A = B
        B = temp
    while B != 0:
        rem = A % B
        A = B
        B = rem
    return A


def lcm(a, b):
    return a*b/(gcd(a, b))


y = lcm(70, 12)
x = gcd(105, 1005)
