from typing import List
#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        left=0
        right=0
        # flip first k zeros to 1
        ans=-1
        while left<n:
            c=k
            right=left
            while right<n:
                if nums[right]==1:
                    right+=1
                else:
                    if c>0:
                        c-=1
                        right+=1
                    else:
                        # no possible flips
                        break
            ans=max(right-left,ans)
            break
        # we have a proper window containg min of k elements 
        # move left pointer to next zero, 
        cf=False
        while right<n:
            if nums[right]==1:
                right+=1
            else:
                if cf:
                    right+=1
                    cf=False
                else:
                    ans=max(right-left,ans)
                    if nums[left]==1:
                        while left<n:
                            if nums[left]==1 :
                                left+=1
                            else:
                                break
                    else:
                        cf=True
                        left+=1
        ans=max(right-left,ans)
        return ans
        '''
        # TLE 
        # n=len(nums)
        # left=0
        # right=0
        # # flip first k zeros to 1
        # ans=-1
        # while left<n:
        #     c=k
        #     right=left
        #     while right<n:
        #         if nums[right]==1:
        #             right+=1
        #         else:
        #             if c>0:
        #                 c-=1
        #                 right+=1
        #             else:
        #                 # no possible flips
        #                 break
        #     ans=max(right-left,ans)
        #     left+=1
        # return ans
        '''

# @lc code=end

nums = [1,1,1,0,0,0,1,1,1,1,1] 
k = 2
# Output: 6
# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3
# Output: 10
a=Solution()
x=a.longestOnes(nums,k)
print(x)