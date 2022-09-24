


class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(self, a, b):
        ret = []
        l = len(a)
        if l < b:
            b = b % l
        i = 0
        while i+b < l:
            ret.append(a[i + b])
            i+=1
        i = 0
        while i < b:
            ret.append(a[i])
            i+=1
        return ret


A = [14, 5, 14, 34, 42, 63, 17, 25, 39, 61, 97, 55, 33, 96, 62, 32, 98, 77, 35]
a = Solution()
x=a.rotateArray(A, 56)
print(x)