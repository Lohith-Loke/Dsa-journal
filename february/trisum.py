from tkinter import N


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        su = len(nums)-1
        res=[]
        for i ,a in enumerate(nums):
            if i >0 and a ==nums[i-1]:
                # no dupe
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                sm= a+nums[l]+nums[r]
                if sm>0:
                    r-=1
                elif sm<0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res

s=Solution()
# x=s.threeSum([-1,0,1,2,-1,-4])
x=s.threeSum([0,0,0,0])

print(x)