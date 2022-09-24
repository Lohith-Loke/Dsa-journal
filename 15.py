from typing import List


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # no corner case check needed
        price = [A[0], A[1]+A[0]]
        for i in range(2, len(A)):
            tc = min(price[i-1], price[i-2])
            price.append(tc+A[i])
        return price[-1]


a = Solution()

x=a.solve(A=[4,1,2,3,4])
print(x)