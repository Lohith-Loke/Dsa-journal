# A = [-2, -3, 4, -1, -2, 1, 5, -3]
# solution for max sum from a sub array
# A = [10, -1, 2, 3, -4, 100]

A = [1, 2, 5, -7, 2, 3]
A = [0, 10, -10, 10]


A.append(-1)
d = {}
total = 0
max = -1
subarray = []
lenmax = 0
for i in range(len(A)):
    if A[i] >= 0:
        # sum up
        total += A[i]
        subarray.append(A[i])
        if max <= total:
            max = total
    else:
        z = i+1
        total = 0
        if subarray != []:
            if d.get(max):
                # key present
                d[max].append(subarray)
                subarray = []
            else:
                d[max] = []
                d[max].append(subarray)
                subarray = []
lenmax = -1
l = []
for i in d[max]:
    if len(i) >= lenmax:
        lenmax = len(i)

print(lenmax)
print(d)
