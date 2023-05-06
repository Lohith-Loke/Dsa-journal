#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start




class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        #48 -> 0  57 ->9  
        # print(s)
        negative=False
        i=0
        if s[0]=='-' or s[0]=='+':
            if s[0]=='-':
                negative=True
            i=1
        
        while i <len(s):
            x=ord(s[i])
            if x>47 and x<58:
                num=num*10 + x-48
                flag= True
            else:
                if num==0:
                    break
                if flag:
                    break
            i+=1
        intmax=2**31
        if negative:
            num=num*-1

        if num>intmax:
            return intmax
        if num<intmax*-1:
            return -intmax*-1
        return num

# @lc code=end
a=Solution()
num=a.myAtoi("0----9")
print(num)