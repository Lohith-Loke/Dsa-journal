import math

class Solution:
	# @param A : integer
	# @return a list of integers
	def isprime(self, num):
		if num == 2:
			return True
		if num == 1:
			return False
		n = int(math.sqrt(num))+1
		for i in range(2, n):
			if  num% i == 0:
				return False
		return True

	def sieve(self, A):
		l=[]
		for i in range(1,A):
			if (self.isprime(i)):
				l.append(i)
		
		return l    
			
a=Solution()
x=a.sieve(10)
print(x)