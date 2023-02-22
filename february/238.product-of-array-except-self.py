#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre=[1]
        p=1
        for i in range(len(nums)-1):
            p=p*nums[i]
            pre.append(p)
        p=1
        for i in range(len(nums)-1,-1,-1):
            pre[i]=pre[i]*p
            p=p*nums[i]
        return pre

# @lc code=end
nums = [1,2,3,4]
a=Solution()
op=a.productExceptSelf(nums)
print(op)