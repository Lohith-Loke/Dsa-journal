class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        ln = len(A)
        b = []
        for c in range(ln):
            l = []
            for i in A:
                l.append(i[c])
            b.append(l)
        return b


b = [[1, 0],
     [1, 0]]
a = Solution()
z = a.solve(b)
for i in z:
    print(i)
