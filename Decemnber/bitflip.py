
class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        st=format(A,'b')
        num="0"*(32-len(st)) +st
        num=num[::-1]
        return int(num,2)
a=Solution()
x=a.reverse(2)

# x=a.reverse(1073741824)
print(x)