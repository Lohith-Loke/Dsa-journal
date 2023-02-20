from cgitb import small
import heapq

# https://leetcode.com/problems/find-median-from-data-stream/
class MedianFinder(object):

    def __init__(self):
        self.small=[] # min geap 
        self.large=[] # max heap 

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # check the num
        if num<self.small[0]:
            heapq.heappush(self.small,num)
        else:
            heapq.heappush(self.large,num*-1) 
        
        if abs(len(self.small)-len(self.large))>1:
            # we need balencing 
            if len(self.small)<len(self.large):
                # small has more elements pop one and add to large 
                heapq.heappop(self.large)
            


    def findMedian(self):
        """
        :rtype: float
        """
        pass
        

# Your MedianFinder object will be instantiated and called as such:
medianFinder=MedianFinder()
medianFinder.addNum(1)  
medianFinder.addNum(2)     
medianFinder.findMedian()
medianFinder.addNum(3)      
medianFinder.findMedian() 
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()