#   945. Minimum Increment to Make Array Unique
import collections

class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx=max(nums)
        cnt=collections.Counter(nums)
        taken =[]
        moves=0
        for i in range(len(nums)+mx):
            if cnt[i]>2:
                taken.extend([x]*(cnt[x]-1))
            elif taken and cnt[x]==0:
                moves+=x-taken.pop()
        return moves
        
#      0 1 2 
nums =[0,2,2,2]
a=Solution()
x=a.minIncrementForUnique(nums)
print(x)
