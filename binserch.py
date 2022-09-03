class Solution:
    def binserch(a):
        pass 
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        for i in range(len(A)):
            if A[i] >B:
                return i 
        return i+1


a= Solution()
a.solve([1,2,3,4,5,6,7,8,9,10],11)