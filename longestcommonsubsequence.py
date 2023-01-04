#!/usr/bin/env python3

#text1 = "abcde"
#text2 = "ace"
#Output: 3


#text1 = "abc", text2 = "abc"
#Output: 3
# txt1="psnw"
# txt2="vozsh"
# output =1
class Solution:

    def sol(self, txt1: str, txt2: str) -> int:
        l1 = len(txt1)
        l2 = len(txt2)
        dk={}
        l1islonger = False
        if l1 > l2:
            l1islonger = True
            # make a dict of l2
            for i in txt1:
                dk[i]=1
        else:
            # make a dict of l1
            for i in txt1:
                dk[i]=1
        i = j = 0
        c = 0
        while (i != l1 and j != l2):
            if txt1[i] == txt2[j]:
                c += 1
                i += 1
                j += 1
            else:
                if l1islonger:
                    #txt 1 is longer so incriment i
                    i += 1
                else:
                    #txt 2 is longer so inciment j
                    j += 1
        return c


if "__main__" == __name__:
    text2 = "abc"
    text1 = "def"
    a = Solution()
    res = a.sol(text1, text2)
