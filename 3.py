from typing import List


class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:
      list=[nums[0]]
      for i in range(1,len(nums)):
        list.append(list[i-1]+nums[i])
      print(list)
    

a = Solution()
a.runningSum(nums=[3, 1, 2, 10, 1])
