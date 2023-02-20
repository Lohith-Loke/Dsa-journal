#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d1={}
        dk=Counter(nums)
        hp=[]
        for i in dk.keys():
            if dk[i] in d1:
                d1[dk[i]].append(i)
                continue
            d1[dk[i]]=[i]
        # print(d1)
        lst=list(d1.keys())
        lst.sort(reverse=True)
        sol=[]
        for i in range(len(lst)):
            for j in d1[lst[i]]:
                k-=1
                sol.append(j)
            if k==0:
                return sol
    
# @lc code=end


nums = [1,1,1,2,2,3]
nums=[1,1,1,2,2,2,3,3,3]
k = 3
#   Output: [1,2]
a=Solution()
x=a.topKFrequent(nums,k)
print(x)