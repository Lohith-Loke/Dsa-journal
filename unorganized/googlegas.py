# %%/


class Solution:
	def solvethis(self, lst, i):
		l = len(lst)-1
		k = i
		bal = 0
		second = False
		while True:
			if i > l:
				# set to 0
				i = 0
				return True
				second = True
				continue
			if second:
				if i == k:
					break
			bal = bal+lst[i]
			i += 1
			if bal < 0:
				k=k+1
				break
		if i == k:
			return True
		return False

	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return an integer
	def canCompleteCircuit(self, A, B):
		if sum(A) < sum(B):
			return -1
		p = []
		for i in range(len(A)):
			p.append(A[i]-B[i])
		print(p)
		t=0
		r=0
		for i in range(len(p)):
			# if (self.solvethis(p[:], i)):
			# 		return i
			t+=p[i]
			if t<0:
				r=i+1
				t=0
		return r

a = Solution()
z = a.canCompleteCircuit([1,2,3], [2,1,2])
print("index= ", z)
# %%
