class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def solve(self, A, B):
			lc,lr=8,8
			i ,j =1,1
			count=0 
			#to bottom left 
			while True :
				if A+i<=8 and B+i<=8:
					i=i+1
					count+=1
				else:
					break          
			# top left 
			i,j=1,1
			while True:
				if A-i>0 and B+i<=8:
					i=i+1
					count+=1
				else:
					break
			#to top right 
			i =1
			while True :
				if A-i>0 and B-i>0:
					i+=1
					count+=1
				else :
					break
			#to bottom right 
			i=1
			while True :
				if A+i<=8 and B-i>0:
					i+=1
					count+=1
				else :
					break

			return count 
a=Solution()
x=a.solve(4,4)
print(x)