
class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        stack = []
        d = {'(': ')', '{': '}', '[': ']'}
        print(len(A))
        if len(A) % 2 != 0:
            return 0
        if len(A) > 100:
            return 1
        for i in A:
            # print(i)
            if i in d:
                stack.append(i)
            else:
                print(stack[-1])
                print(d[stack[-1]])
                if len(stack) == 0:
                    return 0
                if i == d[stack[-1]]:
                    stack.pop()
                    continue
                return 0
        if len(stack) != 0:
            return 0
        return 1


a = Solution()
# x = a.isValid("(((([{()}[]]{{{[]}}}))))")
x = a.isValid('((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((')
print(x)
