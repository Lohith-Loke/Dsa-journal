from cv2 import rotate


class Solution(object):
    def roth(self,i ,j, nums):
        while i <j:
            nums[i]= nums[i]^nums[j]
            nums[j]= nums[i]^nums[j]
            nums[i]= nums[i]^nums[j]
            i+=1
            j-=1
        return 
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        i =0
        j= k-1
        self.roth(i,j,nums)
        i=k
        j=len(nums)-1
        self.roth(i,j,nums)

        return nums

arr=[1,2,3,4,5,6,7]
arr2=[5,6,7,1,2,3,4]

a=Solution()

x=a.rotate(arr,3)
print(arr2)
print(x)