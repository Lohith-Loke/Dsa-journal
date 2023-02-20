import heapq
#768. Max Chunks To Make Sorted II
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sm=0 
        sm2=0
        hp=arr.copy()
        hp.sort()
        c=0
        for i in range(len(hp)):
            sm+=arr[i]
            sm2+=hp[i]
            if sm==sm2:
                c+=1
        return c
        



arr=[5,4,3,2,1]
a=Solution()
x=a.maxChunksToSorted(arr)
print(x)