#
# @lc app=leetcode id=73 lang=python
#
# [73] Set Matrix Zeroes
#

# @lc code=start

class Solution(object):
    def rowzero(self,matrix,row):
        matrix[row]=[0]*len(matrix[row])
    def colzero(self,matrix,col):
        for i in range(len(matrix)):
            matrix[i][col]=0
    def setZeroes(self, matrix):
        """ 
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row0,col0=False,False  
        i=0
        j=0 # skip first element 
        while i<len(matrix):
            while j<len(matrix[i]):
                if matrix[i][j]==0:
                    if j!=0:
                        matrix[i][0]=0
                        matrix[0][j]=0
                    else:
                        col0=True
                j+=1
            j=0
            i+=1

        for i in range(1,len(matrix[0])):
            if matrix[0][i]==0:
                self.colzero(matrix,i)    
        for i in range(0,len(matrix)):
            if matrix[i][0]==0:
                self.rowzero(matrix,i)
        if col0:
            self.colzero(matrix,0)
        return matrix
# @lc code=end