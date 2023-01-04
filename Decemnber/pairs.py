

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        B=abs(B)
        A.sort()
        low = 0 
        high = 1
        while (high!= len(A)) and (low!=len(A)):
            if (high>low) and  abs(A[high]-A[low])==B:
                return 1 
            else:
                if(high<=low or ( A[high]-A[low]<B)):
                     high+=1
                else:
                    low+=1
        return 0

A=[ 20, 500, 1000, 200 ]
B=9
a=Solution()
x=a.solve(A,B)
print(x)