'''
2148. Count Elements With Strictly Smaller and Greater Elements
'''
class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx=max(nums)
        mn=min(nums)
        c=0
        for i in nums:
            if i !=mn and  i != mx:
                c+=1
        return c
            
arr=[11,7,2,15]
a=Solution()
x=a.countElements(arr)
print(x)