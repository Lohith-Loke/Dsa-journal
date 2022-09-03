class Solution:
    def tobinary(self, num, l=[]):
        if num > 1:
            self.tobinary(num//2, l)
        l.append(num % 2)
        # print (num % 2,end="")
        return l

    # @param A : integer
    # @return an integer
    def solve(self, A):
        l = self.tobinary(A)
        # to decimal with bit flip
        num = 0
        power = 0
        # print(l)
        for i in range(len(l)-1, -1, -1):
            # reverse loop iteration
            if l[i] == 0:
                l[i] = 1
            else:
                l[i] = 0
            num = num+l[i]*(2**power)
            power += 1

        return num

a=Solution()
c=a.solve(7)
