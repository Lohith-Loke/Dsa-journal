#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)<=k:
            return "0"
        ar=[int(i) for i in num]
        stk=[]
        i=0
        while i<len(ar):
            if stk:
                while stk and k>0:
                    if stk[-1]>ar[i]:
                    #process the stk[-1]
                        stk.pop()
                        k-=1
                    else:
                        break
            if not stk:
                if ar[i]==0:
                    i+=1
                    continue
                
            stk.append(ar[i])
            i+=1
        # if its increasing sequence , we need to remove last element
        while k>0:
            if stk:
                stk.pop()
                k-=1
            else:
                break
        if stk:
            return "".join([str(stk[j]) for j in range(len(stk))])
        return "0"
# @lc code=end


# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to 
# form the new number 1219 which is the smallest.
a=Solution()
s=a.removeKdigits(num = "100", k = 1)
print(s)
