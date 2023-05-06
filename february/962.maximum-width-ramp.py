#
# @lc app=leetcode id=962 lang=python
#
# [962] Maximum Width Ramp
#

# @lc code=start
class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx=-1
        stk=[]
        for i in range(len(nums)-1,-1,-1):
            print(nums[i])
            j=0
            while True:
                if nums[i]<=stk[j]:
                    mx=max(mx,i+1+len(stk)-i)
                        
            
            stk.append(nums[i])
            
        
# @lc code=end
arr=[6,0,8,2,1,5]
a=Solution()
# x=a.maxWidthRamp(arr)
# print(x)

