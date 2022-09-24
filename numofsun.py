
class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        week = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
        i = week.index(A)
        if B > 7:
            if i == 6:
                return int(B/7)+1
            else:
                return int(B/7)
        if B < 7:
            if i == 6:
                return 1
            c = 6-i
            if c < B:
                return 1
            return 0
        return 1


a = Solution()
x = a.solve("Saturday", 11)
print(x)
