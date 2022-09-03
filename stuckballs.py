
from typing import List


class Solution:
    def search(self, grid: List[List[int]], column, r) -> List[int]:
        gotstuck = False
        r, c = len(grid)-1, len(grid[0])-1
        level = 0
        while True:
            if level > r:
                break
            if grid[level][column] == 1:
                # its right side check \
                if column+1 > c:
                    # \ |
                    gotstuck = True
                    break
                if grid[level][column+1] == 1:
                    # \ \
                    column = column+1
                    level += 1
                else:
                    # \/
                    gotstuck = True
                    break
            else:
                # check left side /
                if column - 1 < 0:
                    # | /
                    gotstuck = True
                    break
                if grid[level][column-1] == -1:
                    # / /
                    level = level+1
                    column = column-1
                    continue
                else:
                    #  \/
                    gotstuck = True
                    break
        r = column
        return gotstuck, column

    def findBall(self, grid: List[List[int]]) -> List[int]:
        result = [0]*len(grid[0])
        r = 0
        for i in range(len(grid[0])):
            gotstuck, r = self.search(grid, i, r)
            if gotstuck:
                result[i] = -1
                continue
            result[i] = r

        return result


a = Solution()
c = [[1, 1, 1, 1, 1, 1],
     [-1, -1, -1, -1, -1, -1],
     [1, 1, 1, 1, 1, 1],
     [-1, -1, -1, -1, -1, -1]]

x = a.findBall(c)
print(x)
