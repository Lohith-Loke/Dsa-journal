
class Solution:
    def solve(self, A):
        top = right = 0
        bottom = len(A)-1
        left = len(A[0])-1
        res = []
        while True:
            if (right > left):
                break
            for i in range(right, left+1):
                res.append(A[top][i])
            top += 1

            if top > bottom:
                break
            for i in range(top, bottom+1):
                res.append(A[i][left])
            left -= 1
            if left < right:
                break
            for i in range(left, right-1, -1):
                res.append(A[bottom][i])
            bottom -= 1
            if bottom < top:
                break
            for i in range(bottom, top-1, -1):
                res.append(A[i][right])
            right += 1
        return res


b=[
  [1, 2],
  [3, 4],
  [5, 6],
]
a = Solution()
x = a.solve(b)
if x == None:
    exit()
print(x)
