class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        j = 0
        i = B
        mx = 0
        islimit = True
        while True:
            temp = A[j:i]
            c = 0
            for k in temp:
                if k == 'a':
                    c += 1
            mx = max(mx, c)
            j = i
            i = i+B
            if j >len(A)-1:
                break
            if  mx == B:
                break
        return mx


a = Solution()
c = a.solve("bab", 2)
print(c)
