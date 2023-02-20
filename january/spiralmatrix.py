# Spirally traversing a matrix
#User function Template for python3


class Solution:

	#Function to return a list of integers denoting spiral traversal of matrix.
	def spirallyTraverse(self,matrix, r, c): 
		# code here 
		top = 0 
		down =r-1
		left=0 
		right= c-1
		while top>=down and left>=right:
			pass


matrix=[
	[1,2,3,4],
	[12,13,14,5],
	[11,16,15,6],
	[10,9,8,7]
]
a=Solution()
a.spirallyTraverse(matrix,len(matrix),len(matrix[0]))