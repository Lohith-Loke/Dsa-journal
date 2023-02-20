#
# @lc app=leetcode id=179 lang=python
#
# [179] Median of Two Sorted Arrays
#

# @lc code=start
from functools import cmp_to_key

class LargerStrKey(str):
  def __lt__(x, y):
    return x + y > y + x
class Solution(object):

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        return ''.join(sorted(map(str, nums), key=LargerStrKey)).lstrip('0') or '0'
# @lc code=end