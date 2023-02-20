from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k==1:
            return nums
        q= deque() 
        q.append(0)
        arrmx=[]
        lim=0
        i=1
        while i<len(nums):
            if nums[q[-1]]<nums[i]:
                while q:
                    if nums[q[-1]]<nums[i]:
                        q.pop()
                    else:
                        break
                q.append(i)
            else:
                q.append(i)
            
            if i>=k-1:
                if k==i-q[0]:
                    q.popleft()
                arrmx.append(nums[q[0]])
            i+=1
            #arrmx.append(q[-1])
        return arrmx
k=2
arr=[7,2,4]
a=Solution()
x=a.maxSlidingWindow(arr,k)
print(x)