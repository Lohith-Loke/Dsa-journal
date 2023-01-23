# class Solution:
# 	def ngs(self,A):		
# 		s=[]
# 		res=[0]*len(A)
# 		s.append(0)
# 		for i in (len(A)-1,-1,-1):
# 			while s and s[-1] <= A[i]:
# 				s.pop()
# 			if s:
# 				res[i]=s[-1]
# 			else:
# 				res[i]= -1
# 			s.append(A[i])
# 		return res		

def printNGE(arr):
	s = []
	element = 0
	res=[]
	s.append(arr[0])
	for i in range(1, len(arr), 1):
		if s:
			element = s.pop()
			while element < arr[i]:
				res.append(arr[i])
				if not s :
					break
				element = s.pop()
			if element > arr[i]:
				s.append(element)
		s.append(arr[i])
	while s:
		res.append(-1)
		s.pop()
	print(arr)
	print(res)

# Driver code
arr = [7, 8, 1, 4]
printNGE(arr)
A=[ 4 , 6, 2 ,7 ,2 ,25]