import string
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if len(A)< 8 or len(A)> 15:
            return 0
        hasnum=False
        hascap=False
        haslow=False
        hasspsl=False
        dk={}
        for i in string.punctuation:
            dk[i]=None
        for i in A:
            if not hasnum:
                if i.isdigit():
                    hasnum=True
                    continue
            if not hascap:
                if i.isupper():
                    hascap=True
                    continue
            if not haslow:
                if i.islower():
                    haslow=True
                    continue
            if not hasspsl:
                if i in dk:
                    hasspsl=True
                    continue
            if (hasspsl and haslow and hascap and hasnum):
                return 1
        if (hasspsl and haslow and hascap and hasnum):
            return 1
        return 0
A="Scaler@1"
a=Solution()
x=a.solve(A)
print(x)