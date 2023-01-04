class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        binary = []
        while A!=0:
            q=A%2
            binary.append(q)
            A=A//2
        print(binary)
        # we need first 1 from R to L
        i=0
        while i<len(binary):
            if binary[i] == 1:
                break
            i+=1
        return i

a=Solution()
x=a.solve(18)
print(x)