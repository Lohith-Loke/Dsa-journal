import heapq
import math
class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        h=[]
        for value in gifts:
            heapq.heappush(h, -1*value)
        for _ in range(k):
            x=heapq.heappop(h)
            heapq.heappush(h,-1*int(math.sqrt(x*-1)))
            heapq.heapify(h)
        return -1*sum(h)
s=Solution()
ans=s.pickGifts([25,64,9,4,100], 4)
print(ans)