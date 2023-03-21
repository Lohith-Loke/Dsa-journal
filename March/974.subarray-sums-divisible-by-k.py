#
# @lc app=leetcode id=974 lang=python
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
from itertools import count


class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans=0
        d={0:1}
        prvsum=0
        for i in range(len(nums)):
            prvsum+=nums[i]
            key=prvsum%k
            if key in d:
                ans+=d[k]
                d[k]+=1
            else:
                d[k]=1
        
        return ans
# @lc code=end
a=Solution()
a.subarraysDivByK([4,5,0,-2,-3,1],k=5)
