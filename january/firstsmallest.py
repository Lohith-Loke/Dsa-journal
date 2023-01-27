# 41. First Missing Positive

class Solution(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # no -ve values
        ln=len(nums)  
        for i in range(ln):
            if nums[i]<0:
                nums[i]=0

        for i in range(ln):
            idx=abs(nums[i])
            
            if idx<=ln and idx>0:
                if nums[idx-1]>0:
                    nums[idx-1]=nums[idx-1]*-1
                else:
                    if nums[idx-1]==0:
                        nums[idx-1]=(ln+1)*-1
        
        for i in range(ln):
            if nums[i]>=0:
                return i+1
        
        return ln+1
        
nums = [3,3,1,4,0]
a=Solution()
x=a.firstMissingPositive(nums)
print(x)