class Solution:

    def ithodd(self, A: int):
        return (2 * A - 1)

    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        ln = self.ithodd(A)
        lst = [A] * ln
        bglst = []
        bglst.append(lst[:])
        i = 1
        while (True):
            if i >= ln / 2:
                break
            lst[i] = A - 1
            i += 1
            bglst.append(lst[:])
        if A > 1:
            bglst.append(bglst[0])
        print(bglst)


a = Solution()
print(a.prettyPrint(2))