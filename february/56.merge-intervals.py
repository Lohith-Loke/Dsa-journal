#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#

# @lc code=start
class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # make a dictionary of end time  if encounter start time less than end time merge them 
        # remove prevoous endtime  the end time after 
        intervals.sort()
        sol=[intervals[0]]
        for start,end in intervals:
            if end <=sol[-1][1]:
                # if end is less than end of
                # pre we should skip this interver
                continue
            if sol[-1][1]>=start:
                # if end of prv is > than start # merge the intervels   
                sol[-1][1]=max(sol[-1][1],end)
            else:
                # if all above case is missed its intervel with no 
                # intersection 
                sol.append([start,end])
        return sol

# @lc code=end
a=Solution()
a.merge([[1,4],[0,4]])


