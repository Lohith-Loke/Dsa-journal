# isomorphic strings

class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}

        for i in range(len(s)):
            if d.get(s[i]):
                # if maping exist check if its correct
                if d[s[i]] != t[i]:
                    return False

            # no entry so map data
            d[s[i]] = t[i]

        d2 = {}
        for i in range(len(s)):
            if d2.get(t[i]):
                # if maping exist check if its correct
                if d2[t[i]] != s[i]:
                    return False
            # no entry so map data
            d2[t[i]] = s[i]
        return True


a = Solution()
print(a.isIsomorphic("paper", "title"))
