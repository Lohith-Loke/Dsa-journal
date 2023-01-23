'''
Given a binary array A, find the maximum sequence of continuous 1's that can be formed by replacing at-most B zeroes.
For this problem, return the indices of maximum continuous series of 1s in order.
If there are multiple possible solutions, return the sequence which has the minimum start index.
'''
A = [1,1 ,0 ,1, 1, 0, 0, 1, 1, 1 ]
B = 1
ans =[0, 1, 2, 3, 4]
# A = [1, 0, 0, 0, 1, 0, 1]
# B = 2
# ans= [3, 4, 5, 6]

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        c=B
        i=0
        # find first limit 
        while i<len(A):
            if A[i]==0:
                if c!=0:
                    c-=1
                else:
                    break
            i+=1
        mxidx=0
        mxln=ln=i
        i=1
        prv=A[0]
        # find all limit 
        while i<len(A):
            if prv==0:
                j=i+ln-1
                c=1
                while j<len(A):
                    if A[j]==0:
                        if c!=0:
                            c-=1
                        else:
                            break
                    j+=1
                # we moved j steps ahead len of sub array 
                ln=j-i
                if ln>mxln:
                    mxidx=i
                    mxln=ln
            else:
                ln-=1
            # if we have arr less than mx len we dont need to look for longest its not present there 
            if i+mxln>len(A):
                break
            prv=A[i]
            i+=1
        return [i for i in range(mxidx,mxln+mxidx)]
a=Solution()
x=a.maxone(A,B)
print(x)