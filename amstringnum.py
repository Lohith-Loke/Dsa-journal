class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        b=A
        lst=[]
        while A!=0:
            rem = A%10
            A=int(A/10)
            lst.append(rem)
        s=0
        for i in lst:
            s=s+pow(i,len(lst))
        if s==b:
            return 1
        return 0
a=Solution()
a.solve(371)