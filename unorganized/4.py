# pivoit index 
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        i = 0
        Rightsum = 0
        try:
            while True:
                if Rightsum == (S-Rightsum-nums[i]):
                    return i
                Rightsum=Rightsum+nums[i]
                i = i+1
            return -1
        except:
            return -1


a = Solution()
a.pivotIndex([1,2,3])

# 1,7,3,6,5,6
