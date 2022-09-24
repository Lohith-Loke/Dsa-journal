def solve(A, B):
    # find sum of first b elements
    s = sum(A[:B])
    if B == len(A)-1:
        return s
        # return it if b= len(a)-1
    m = s
    print(A[:B])
    for i in range(B):
        # subtract last added num form sum
        s -= A[B-1-i]
        print("sum - ", A[B-1-i])
        print("sum plus ", A[len(A)-1-i])
        # add last num form array
        s += A[len(A)-1-i]
        m = max(m, s)
        # if new max is found keep it
    return m


A = [1, 2, 3, 2, 5]
B = 3

x = solve(A, B)
print()
print(x)
