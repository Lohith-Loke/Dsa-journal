from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        right,bottom = len(matrix[0])-1, len(matrix)-1
        left, top = 0, 0
        s = []
        while True:
            if left > right:
                break
            
            for i in range(left, right+1):
                print(matrix[top][i])
                s.append(matrix[top][i])
            top += 1

            if top > bottom:
                break

            for i in range(top, bottom+1):
                print(matrix[i][right])
                s.append(matrix[i][right])
            right -= 1

            if left > right:
                break
            
            for i in range(right, left-1, -1):
                print(matrix[bottom][i])
                s.append(matrix[bottom][i])
            bottom -= 1

            if top > bottom:
                break

            for i in range(bottom, top-1, -1):
                print(matrix[i][left])
                s.append(matrix[i][left])
            left += 1
        return s


a = Solution()

x = a.spiralOrder(
    [[7], [9], [6]]
)
print(x)
