class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):
		i = 0
		j = 1
		profit = 0
		maxpro=max(A)-min(A)
		while True:
			
			if i+1 > len(A)-1:
				break
			diff=0
			mx=max(A[i+1:])
			
			if A[i] < mx:
				# buy in i and sell in j
				
				diff = mx-A[i]
				print("diff=",mx,"-",A[i],"=",diff)

			profit=max(diff,profit)
			if profit==maxpro:
				return profit
			i += 1
		return profit

a=Solution()
print(a.maxProfit([0,0,0]))
