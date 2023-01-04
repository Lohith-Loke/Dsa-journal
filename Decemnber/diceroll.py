A = 2
# Ways to get sum 2 are {1, 1} {2}.
ans= 2
A = 3
# Ways to get sum 3 are {1, 1, 1}, {1, 2}, {2, 1}, {3}
ans = 4
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # represent A as sum of k numbers from  [1,6] 
        x=[1]*A
        # sums up to A 
                    