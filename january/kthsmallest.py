import heapq

class Solution:
    def kthSmallest(self,arr, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        hp=[]
        for i in arr:
            heapq.heappush(hp,i)
        for i in range(k):
            print(hp)
            x=heapq.heappop(hp) 
        return x 
        
arr=[7,10,4,3,20,15]
# arr=[7 10 4 3 20 15]
a=Solution()
x=a.kthSmallest(arr,3)
print(x)