#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        memo = [[False]*n for _ in range(n)]
        start = 0
        max_len = 1

        # Base cases: single characters are palindromes
        for i in range(n):
            memo[i][i] = True

        # Base cases: adjacent characters are palindromes
        for i in range(n-1):
            if s[i] == s[i+1]:
                memo[i][i+1] = True
                start = i
                max_len = 2

        # General cases: build memoization table bottom-up
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i+k-1
                if s[i] == s[j] and memo[i+1][j-1]:
                    memo[i][j] = True
                    if k > max_len:
                        start = i
                        max_len = k

        return s[start:start+max_len]


# @lc code=end

a=Solution()
x=a.longestPalindrome("dtgrtoxuybwyfskikukcqlvprfipgaygawcqnfhpxoifwgpnzjfdnhpgmsoqzlpsaxmeswlhzdxoxobxysgmpkhcylvqlzenzhzhnakctrliyyngrquiuvhpcrnccapuuwrrdufwwungaevzkvwbkcietiqsxpvaaowrteqgkvovcoqumgrlsxvouaqzwaylehybqchsgpzbkfugujrostopwhtgrnrggocprnxwsecmvofawkkpjvcchtxixjtrnngrzqpiwywmnbdnjwqpmnifdiwzpmabosrmzhgdwgcgidmubywsnshcgcrawjvfiuxzyzxsbpfhzpfkjqcpfyynlpshzqectcnltfimkukopjzzmlfkwlgbzftsddnxrjootpdhjehaafudkkffmcnimnfzzjjlggzvqozcumjyazchjkspdlmifvsciqzgcbehqvrwjkusapzzxyiwxlcwpzvdsyqcfnguoidiiekwcjdvbxjvgwgcjcmjwbizhhcgirebhsplioytrgjqwrpwdciaeizxssedsylptffwhnedriqozvfcnsmxmdxdtflwjvrvmyausnzlrgcchmyrgvazjqmvttabnhffoe")
 
print(x)
