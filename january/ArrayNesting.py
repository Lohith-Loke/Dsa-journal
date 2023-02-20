# 565. Array Nesting
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans= 0 
        vis=[0]*len(nums)
        for i in range(len(nums)):
            if vis[i]==0:
                continue
            else:
                mx= 0 
                cur = i
                while vis[cur]==1:
                    cur=nums[cur]
                    mx+=1
                ans= max(ans,mx)
        return mx
        
    