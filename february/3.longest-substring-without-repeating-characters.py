#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        j=0
        maxlen=0
        chars=set()
        while i <len(s):
            if s[i] not  in chars:
                chars.add(s[i])
                i+=1
                maxlen=max(i-j,maxlen)
            else:
                chars.remove(s[j])
                j+=1
        return maxlen
         
# @lc code=end