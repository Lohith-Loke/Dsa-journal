import string
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        A=A.translate(None,string.punctuation)
        A=A.lower() # convert to lower 
        full=string.ascii_lowercase+"1234567890"
        
        dk={}
        for i in full:
            dk[i]=None
        # dictionay contains all alpha numeric chars 
        tmp=""
        A.translate(dk)
        for i in A:
            if i in dk: # accept only alpaha numeric values 
              tmp+=i
        A=tmp
        ln=(len(A)//2) +1
        rev=A[::-1]
        print(A[:ln-1])
        print(rev[:ln-1])
        
        for i in range(ln-1):
            if rev[i]==A[i]:
                continue
            return 0
        return 1

A="AbzbA"
a=Solution()
x=a.isPalindrome(A)
print(x)