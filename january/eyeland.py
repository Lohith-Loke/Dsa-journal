class Solution(object):

    def dfs(self,grid,ptr):
        m,n=len(grid),len(grid[0])
        
        (i,j)= ptr
        top=bottom=right=left=None
        if i+1 <m:
            if grid[i+1][j]=="1":
                top=self.dfs(grid,(i+1,j))
        if j+1<n:
            if grid[i][j+1]=="1":
                right=self.dfs(grid,(i,j+1))
        if j-1>-1:
            if grid[i][j-1]=="1":
                left=self.dfs(grid,(i,j-1))
        if i-1<n:
            if grid[i-1][j]=="1":
                bottom=self.dfs(grid,(i-1,j))

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans=0
        m,n= len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":                
                    right=0
                    bottom=0
                    if j+1<m:
                        right=grid[i][j+1]
                    if i+1<m:
                        bottom=grid[i+1][j+1]
                    if right ==0 and bottom==0:
                        ans+=1
                        grid[i][j]=ans
                    else:
                        grid[i][j]=max(right,bottom)
                else:
                    grid[i][j]=0
        return ans

grid=[
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]]
a=Solution()
x=a.dfs(grid,(0,0))
print(x)