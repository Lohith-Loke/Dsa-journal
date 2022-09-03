class Solution:
    # matrix spiral 
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        top = left = 0
        bottom = len(A) - 1
        right = len(A[0]) - 1
        res = []
        while True:
            if left > right:
                break

            for i in range(left, right+1):
                res.append(A[top][i])
            top = top+1

            if top > bottom:
                break

            for i in range(top, bottom + 1):
                res.append(A[i][right])
            right = right - 1

            if left > right:
                break
            for i in range(right, left - 1, -1):
                res.append(A[bottom][i])
            bottom = bottom - 1

            if top > bottom:
                break

            for i in range(bottom, top - 1, -1):
                res.append(A[i][left])
            left = left + 1
        return res


a = Solution()

x = a.spiralOrder(
    [
        [1, 2],
        [3, 4],
        [5, 6],
    ]
)
print(x)
