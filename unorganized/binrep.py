class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        l = []
        while A != 0:
            rem = A % 2
            A = int(A/2)
            l.append(rem)
        l.reverse()
        s = ""
        for i in l:
            s += str(i)
        return int(s)


a = Solution()

x = a.findDigitsInBinary(4)
print(x)
