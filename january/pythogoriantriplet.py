#User function Template for python3
class Solution:
	def checkTriplet(self,arr, n):
		# code here
		arr.sort()
		for i in range(len(A)):
			arr[i]=arr[i]*arr[i]
		# we need to find optimal a, b,c  such that a=b+c
		# a = arr[-1] largest num 
		# b = arr[0] smallest element 
		# c = arr[-1] second largest num 
		# use 2 pointer aproach to solve this 
		i=0
		j=len(arr)-2
		k=len(arr)-1
		while True:
			# print(k)
			if i==j:
				if k >2:
					k=k-1
					j=k-1
					i=0
				else:
					return False

			sm = arr[i]+arr[j]
			if sm==arr[k]:
				return True
			elif sm>arr[k]:
				j-=1
			else:		
				i+=1
			
A=[3, 4,5, 6, 9]
ans=True
a=Solution()
x=a.checkTriplet(A,len(A))
print(x)