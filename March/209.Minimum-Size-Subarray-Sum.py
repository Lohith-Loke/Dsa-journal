
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """ 
        i,j=0,0
        mn=float("inf")
        sm=nums[0]
        while True:
            if sm>=target:
                mn= min(j-i+1,mn)
                sm-=nums[i]
                i+=1
            else:
                j+=1
                if j<len(nums):
                    sm+=nums[j]
                else:
                    break
        return mn if mn!=float("inf") else 0 


a=[12,28,83,4,25,26,25,2,25,25,25,12]
# a=[2,3,1,2,4,3]
t=700
s=Solution()

l=s.minSubArrayLen(t,a)
print(l)