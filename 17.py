class Solution:
    # @param A : string
    # @return an long
    def solve(self, A):
        i = 0
        l = [0]
        num = -1
        while i < len(A):
            if A[i].isdigit():
                num = int(A[i])
                i += 1
                try:
                    while A[i].isdigit():
                        num = num*10+int(A[i])
                        i += 1
                    raise Exception("append data")
                except Exception as e:
                    # print(e)
                    l.append(num)
            else:
                i += 1
        return sum(l)


A = "a12b34c"
a = Solution()
print(a.solve(A))

# print(A.split())
