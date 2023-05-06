#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#

# @lc code=start
class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<2:
            return True 
        if nums[0]==0:
            return False
        i=0
        n=len(nums)-1
        prv=0
        while i<n:
            if nums[i]!=0:

            else:
                i=prv

        
# @lc code=end

nums = [2,3,1,1,4]
a=Solution()
x=a.canJump(nums)
print(x)
