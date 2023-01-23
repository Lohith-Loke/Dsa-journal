class Solution:
	def swap(self,j,i,arr):
		tmp = arr[i]
		arr[i]=arr[j]
		arr[j]= tmp
	#Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
		stk=[]
		i=K
		j=0
		while i<N:
			while i>j:
				self.swap(j,i-1,arr)
				i-=1
				j+=1
			i+=K
		return arr
N = 4
K = 3
arr = [5,6,8,9]
#Output: 8 6 5 9
a=Solution()
x=a.reverseInGroups(arr,N,K)