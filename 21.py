

# A = [-2, -3, 4, -1, -2, 1, 5, -3]
# solution for max sum from a sub array
# A = [10, -1, 2, 3, -4, 100]
# A=[1, 2, 5, -7, 2, 3]
A = [-1]
A = [0, 0, -1, 0]
s = 0
max = -1
c = 0
iszeromax = False
b, z, k = 0, 0, 0
for i in A:
    if i >= 0:
        s = s+i
        if s >= max:
            b = c
            max = s
            k = z
            iszeromax = True
    else:
        z = c+1
        s = 0
    c += 1
if max < 0:
    print([])
print(A[k:b+1])
