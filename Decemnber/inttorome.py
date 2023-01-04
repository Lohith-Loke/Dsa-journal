#
'''
I - 1 
V - 5 
X - 10 
L - 50 
C - 100
D - 500
M - 1000
'''
#  1 <=  A  <= 3999
class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        dk={
            1:"I",
            5:"V",
           10:"X",
           50:"L",
          100:"C",
          500:"D",
         1000:"M"
        }  
        if A in dk :
            # if A is special number 
            return dk[A]
        
        num=[1, 5, 10, 50, 100, 500,1000]
        for i in range(len(num)):
            if A<num[i]:
                break
        
        # we got upper and lower bound of A 
        # num[i-1] <  A  < num[i] 
        





A=5
a= Solution()
a.intToRoman(A)