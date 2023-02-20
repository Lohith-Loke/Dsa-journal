class Solution:
	def countTriplet(self, A, n):
		# code here
		# uae 3 pointer aproach to solve 
		# A +B= c
		if len(A)<2:
			return 0
		A.sort()
		i = 0        # A
		j = len(A)-2 # B
		k = len(A)-1 # sm
		c=0
		while True:
			if i == j:
				if k>=2:
					k=k-1
					j=k-1
					i=0
					if k <2:
						break
				else:
					break

			sm = A[i]+A[j]
			if sm ==A[k]:
				c += 1
				j-= 1
			else:
				if A[k]>sm:
					i+=1
				else:
					j-=1
		
		return c

arr=[14, 3, 6, 8, 11, 16]
a=Solution()
x=a.countTriplet(arr,len(arr))
print(x)