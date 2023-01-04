from json import encoder
import json
A = '{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'
ans='''{ 
        A:"B",
        C: 
        { 
            D:"E",
            F: 
            { 
                G:"H",
                I:"J"
            } 
        } 
    }
'''
class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        c=0
        i=0
        while i <len(A):
            if A[i] ==('{' or '['):
                print(" "*c+A[i])
            else :
                while A[i] !=",":
                    print(A[i],end="")
                    i+=1
                # i ==","
                print(A[i])
            i+=1

a=Solution()
x=a.prettyJSON(A)
# print(x)