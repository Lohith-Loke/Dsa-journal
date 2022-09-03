# palindromic
class Solution:
    # @param A : string
    # @return an integer
    def flip(self, time):
        rem = time % 10
        return(rem*10+int(time/10))

    def solve(self, A):
        A = A.split(":")
        A = [int(A[0]), int(A[1])]
        count = 0
        while True:
            # flip mins
            mins = self.flip(A[1][:])

print(Solution().flip(59))
