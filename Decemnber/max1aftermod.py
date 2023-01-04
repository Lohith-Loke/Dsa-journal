# Maximum Ones After Modifizerosation

A = [1, 0, 0, 1, 1, 0, 1]
B = 1
#  4


from inspect import isframe


# A = [1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
# B = 2 
# 5 

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        sol=[]
        j=0
        c=B
        while j!=len(A):
            if A[j]==0:
                if c==0:
                    break
                c-=1
                j+=1
            else:
                j+=1
        sol.append(j)
        for i in range(1,len(A)):
            prvele=A[i-1]
            prv_sol=sol[i-1]
            if prvele==1:
                # number of zeros is same 
                # endpoint is same so lenth -1
                sol.append(prv_sol-1)
            else:
                 # number is zero 
                j=i+prv_sol-1
                c=1
                while j<len(A):
                    if A[j]==0:
                        if c==0:
                            break
                        c-=1
                        j+=1
                    else:
                        j+=1                
                sol.append(j-i)
        # print(sol)
        return max(sol)
 
a=Solution()
x=a.solve(A,B)
print(x)