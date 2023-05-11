from typing import List

#
# @lc app=leetcode id=75 lang=python3
#
# [75] sort-colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using 3 pointer aproach 
        low=0
        high=len(nums)-1
        mid=low

        while mid<high+1:
            # print(low,mid,high)
            # print(nums)
            if nums[mid]==0:
                # its in right place 
                nums[mid],nums[low]=nums[low],nums[mid]
                if mid==low:
                    mid+=1
                low+=1
                
            elif nums[mid]==2:
                # swap the nums
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
            elif nums[mid]==1:
                mid+=1
        return
        # counting sort method 
        # count freq of nums , replace nums with sorted count 
        m=[0,0,0]
        for i in nums:
            m[i]=m[i]+1
        print(m)
        k=0
        i=0
        while k<3:
            if m[k]!=0:
                nums[i]=k
                i+=1
                m[k]-=1
            else:
                k+=1
# @lc code=end
nums = [2,0,2,1,1,0]
#  [0,0,1,1,2,2]
# nums = [2,1]
#[0,1,2]
a=Solution()
print(nums)
a.sortColors(nums)
print(nums)