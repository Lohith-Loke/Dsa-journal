#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#

# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        mp={}
        i=0
        j=0
        for ch in s:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
# @lc code=end

