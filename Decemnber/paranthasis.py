# A = "())"
# ans= 1
# A = "((("
# ans=3
A=")("

A="(((()"

class Solution:
    # @param A : string
    # @return an integer
    
    def solve(self, A):
        i=0
        st=[]
        c=0
        while i <len(A):
            if A[i]=='(':
                st.append(A[i])
                c+=1
            else:
                if st:
                    st.pop()
                    c-=1

                else:
                    # ) without (
                    c+=1
            i+=1

        return abs(c)
a=Solution()
x=a.solve(A)
print(x)
            