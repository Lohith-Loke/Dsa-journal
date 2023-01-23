class Solution:	
	def binSearch(self, array=[], x=-1, low=0, high=1000):
		# Repeat until the pointers low and high meet each other
		while low <= high:
			mid = low + (high - low)//2
			if array[mid] == x:
				return array[mid]
			elif array[mid] < x:
				low = mid + 1
			else:
				high = mid - 1
		return -1
	def binarysearch(self, arr=[], n=-1, k=1000000):
		# code here
		return self.binSearch(arr,k,0,len(arr))


x=[2, 3, 4, 5, 7, 8, 9, 11, 12, 14, 15, 19, 20, 22, 25, 26, 28, 32, 33, 35, 36, 37, 38, 41, 43, 44, 45, 46, 49, 50, 51, 52, 53, 55, 59, 60, 61, 62, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 88, 92, 93, 94, 95, 96, 98, 99]
s=Solution()
x=s.binarysearch(arr=x,n=len(x),k=88)
print(x)