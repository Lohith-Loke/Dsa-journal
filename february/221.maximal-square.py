#
# @lc app=leetcode id=221 lang=python
#
# [221] Maximal Square
#

# @lc code=start
class Solution(object):
    def issqre(self,mat,start,end):
        (x1,y1)=start
        (x2,y2)=end
        if x1==x2 and y1==y2:
            return True if (mat[x1][y1]==1) else False
        # do a row and colum look of to conform the square 
        i = x1
        j = y1
        while i<len(mat):
        return True

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        nrows=len(matrix)
        ncols=len(matrix[0])
        mx=-1
        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j]==1:
                    k=i+1
                    l=j+1
                    while k <nrows and l<ncols:
                        if matrix[k][l]!=1:
                            break
                        

# @lc code=end
mat=[
    [1,1,0],
    [1,1,0],
    [1,1,0],
]
start=(0,0)
end=(2,2)
a=Solution()
x=a.issqre(mat,start,end)
print(x)
