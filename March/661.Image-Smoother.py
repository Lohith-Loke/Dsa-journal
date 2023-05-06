
class Solution(object):

	def imageSmoother(self, img):
		"""
		:type img: List[List[int]]
		:rtype: List[List[int]]		
		"""
		# (m*n )
		m,n= len(img),len(img[0])
		res=[]
		for i in range(m):
			z=[]
			for j in range(n):
				tot=0
				c=0
				for k in range(max(0,i-1),min(m,i+2)):
					for l in range(max(0,j-1),min(n,j+2)):
						tot+=img[k][l]
						c+=1
				z.append(tot//c)
			res.append(z)

		return res

s=Solution()
img=[[1,1,1],[1,0,1],[1,1,1]]

y=s.imageSmoother(img)
print(y)
