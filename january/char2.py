class Solution(object):            
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk=[]
        i=0
        while i<len(s):
            if s[i]!=']':
                stk.append(s[i])
            else:
                substr=""
                while stk[-1] !='[':
                    substr=stk.pop()+substr
                stk.pop()
                num=""
                while stk:
                    if stk[-1].isdigit():
                        num=stk.pop()+num
                    else:
                        break
                stk.append(int(num)*substr)
            i+=1
        return ''.join(stk)
a=Solution()
z=a.decodeString("100[leetcode]") 
print(z) 