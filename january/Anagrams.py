class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        dk={}
        dk2={}
        for j in range(len(p)):
            if p[j] in dk:
                dk[p[j]]+=1
            else:
                dk[p[j]]=1
        j= 0
        for key in dk.keys():
            dk2[key]=0
            j+=1
        # j
        for i in range(len(s)):
            
            if s[i] in dk2:    
                dk2[s[i]]+=1
            else:
                pass
                
a=Solution()
x=a.findAnagrams("cbaebabacd","abc")
# print(x)