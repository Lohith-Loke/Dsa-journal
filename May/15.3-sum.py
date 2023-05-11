from typing import List
#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def __init__(self):
        self.sol=set()

    def twosum(self,nums,target,id):
        mp=set()

        res=[]
        for idx,i in enumerate(nums):
            if idx == id:
                continue
            inv=target-i

            if inv in mp:

                s=sorted([i,inv,nums[id]])
                if (s[0],s[1],s[2]) not  in self.sol:
                    res.append(s)
                    self.sol.add((s[0],s[1],s[2]))
            else:
                mp.add(i)
        return res

    def threeSum(self, nums: List[int],target:int) -> List[List[int]]:
        # bruteforce appproach 
        res=[]
        for idx,item in enumerate(nums):
            # print(-1*i)
            for i in self.twosum(nums,-1 * item,idx):
                res.append(i)
            # break
        return res
# @lc code=end
nums = [0,0,0] 
target=0
# [[-1,-1,2],[-1,0,1]]
s=Solution()
x=s.threeSum(nums,target)
print(x)