#
# @lc app=leetcode id=792 lang=python
#
# [792] Number of Matching Subsequences
#
# @lc code=start

from collections import defaultdict

class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        
        n_subsequences = 0
        state = defaultdict(list)
        #state={}
        for word in words:
            state[word[0]].append(word[1:])
            #state[word[0]]=word[1:]
        for char in s:
            old_bucket = state[char]
            state[char] = []
            for suffix in old_bucket:
                if not suffix:
                    n_subsequences += 1
                else:
                    state[suffix[0]].append(suffix[1:])
        return n_subsequences
# @lc code=end
a=Solution()
x=a.numMatchingSubseq(s = "abcde", words=["a","bb","acd","ace"])
print(x)