class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # <------
        i=0
        lsm=sum(nums)-nums[i]
        i+=1
        #----->
        rsm=0
        j=len(nums)
        while True:

            print("lsm",lsm)
            print("rsm",rsm) 
            print(i-1)
            if lsm==rsm:
                return i-1
            else:
                if i==len(nums):
                    break
                rsm=rsm+nums[i-1]
                lsm=lsm-nums[i]
            i+=1
        return -1

A=[-1,-1,0,1,1,0] # 5
a=Solution()
x=a.pivotIndex(A)
print(x)