
class Solution(object):
    ncolor=""
    source=""
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        self.source=image[sr][sc]
        self.ncolor=color       
        # image[sr][sc]=color
        self.dfs(image,sr,sc)
        return image
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return
        elif grid[i][j]!= self.source:
            return 
        
        grid[i][j]=self.ncolor
        self.dfs(grid, i+1, j) # top 
        self.dfs(grid, i-1, j) # bottom
        self.dfs(grid, i, j+1) # left
        self.dfs(grid, i, j-1) # right

image =[
[1,1,1],
[1,1,0],
[1,0,1]
]
a=Solution()
x=a.floodFill(image,1,1,2)
for i in x:
    print(i)