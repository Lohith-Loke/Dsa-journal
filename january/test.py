class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid = len(nums)//2
        ctr1=0
        ctr2=0 
        ctr3=0 
        for i in range(len(nums)):
            if nums[i]==nums[mid-1]:
                ctr1+=1
            else:
                if nums[i]==nums[mid]:
                    ctr2+=1
                else:
                    if nums[i]==nums[mid+1]:
                     ctr3+=1
        if ctr1 >= len(nums) +1// 2:
            return nums[mid - 1]
        else:
            if ctr2 >= len(nums) / 2:
                return nums[mid]
            else:
                if ctr3 >= len(nums) / 2:
                    return nums[mid + 1]
        return -1
arr=[3,2,3]
a=Solution()
if 1:
	print("hi")
# print(x)