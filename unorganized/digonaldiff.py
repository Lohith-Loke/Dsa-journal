def diagonalDifference(arr):
    m = len(arr[0]) - 1
    n = len(arr) - 1
    x = y = 0
    sm2 = 0
    while True:
        if x > m or y > n:
            break
        sm2 += arr[x][y]

        x += 1
        y += 1
    y = 0
    x=len(arr[0])-1
    sm = 0
    while True:
        if x == -1 or y > n:
            break
        else:
            sm += arr[x][y]
            x -= 1
            y += 1
    return sm2 - sm if (sm2 - sm) >= 0 else sm - sm2


x = diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])
print(x)