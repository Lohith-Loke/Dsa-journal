class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):
		mn = 100000
		mx = 0
		i = 0
		j = 1
		profit = 0
		while True:
			if j > len(A)-1:
				break
			if A[i] < A[j]:
				print("profit=",A[j],"-",A[i])
				# buy in i and sell in j
				profit += (A[j]-A[i])
			j += 1
			i += 1
		return profit


a = Solution()
print(a.maxProfit([1, 2, 3]))
