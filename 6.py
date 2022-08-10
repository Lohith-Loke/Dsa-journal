# is subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # t is lenthy
        i = 0
        j = 0
        if len(t) == 0:
            if len(s) != 0:
                return False
        try:
            while True:
                if(s[j] == t[i]):
                    j = j+1
                    if(j == len(s)):
                        return True
                i = i+1
                if(i >= len(t)):
                    return False
        except:
            return True


a = Solution()
a.isSubsequence("", "ahbgdc")
