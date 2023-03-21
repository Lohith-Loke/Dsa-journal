#
# @lc app=leetcode id=939 lang=python
#
# [939] Minimum Area Rectangle
#

# @lc code=start
import math
class Solution(object):

    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)<4:
            return 0
        # points contains more than 4 points 
        points_set=set()
        for i in points:
            points_set.add((i[0],i[1]))

        min_area=float("inf")
        for i in range(len(points)):
            x1,y1= points[i]
            for j in range(i+1,len(points)):
                x2,y2=points[j]
                # check if x1!=x2 and y1!=y2
                if x1!=x2 and y1!=y2:
                    if (x1,y2) in points_set and (x2,y1) in points_set:
                        area=abs(x1-x2)*abs(y1-y2)
                        min_area=min(area,min_area)
        return min_area if min_area!=float("inf") else 0 

        
# @lc code=end

