#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if x<0:
            # x=x*-1
        if x <0:
            return False
        num=x
        rev=0
        while x !=0:
            rem=x%10
            q=x//10            
            rev=rev*10+rem
            x=x//10
        if rev == num:
            return True
        return False
        
# @lc code=end
a=Solution()
x=a.isPalindrome(12)
print(x)
