import heapq

class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        
arr=[7,10,4,3,20,15]
arr=[7 ,10, 4, 20, 15]
a=Solution()
x=a.kthSmallest(arr,0,len(arr)-1,4)