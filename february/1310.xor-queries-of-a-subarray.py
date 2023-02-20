#
# @lc app=leetcode id=1310 lang=python
#
# [1310] XOR Queries of a Subarray
#

# @lc code=start
class Solution(object):
	def xorQueries(self, arr, queries):
		"""
		:type arr: List[int]
		:type queries: List[List[int]]
		:rtype: List[int]
		"""

		d1=[0]*len(arr)
		d1.append(1)
		res = []
		for i in range(len(arr)):
			d1[i]=d1[i-1]^arr[i]
		for q in queries:
			s = q[0]
			e = q[1]
			""" see formula induction below"""
			res.append(d1[e] ^ d1[s - 1])
		return res
		
# @lc code=end
arr=[1,3,4,8]
queries=[[0,1],[1,2],[0,3],[3,3]]
a=Solution()
x=a.xorQueries(arr,queries)
print(x)
print("[2 ,7 ,14 ,8]")