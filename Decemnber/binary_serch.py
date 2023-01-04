
class Solutionl:
    def binaryserch(self,A,B,_high,_low=0 ):
        print(" jgcjg")
        _mid= (_high+_low)//2
        if (_high <= _low or _low==len(A)-1):
            ## we don't element  
            return -1

        if A[_mid]>B:
            # we B is in low to mid 
            return self.binaryserch(A,B,_mid,_low)

        if A[_mid]<B:
            # we B is in mid to high 
            return self.binaryserch(A,B,_high,_mid)
            
        if A[_mid] == B:
            return _mid

class Solution:
    
    def binaryserch(self,A,B,low,high):
        mid= (high+low)//2
        if(mid== low or low==len(A)-1):
            ## we don't element  
            return 0

        if B>A[mid]:
            # we B is in low to mid 
            return self.binaryserch(A,B,mid+1,low)

        if B< A[mid]:
            # we B is in mid to high 
            return self.binaryserch(A,B,mid-1,high)
        
        if A[mid]== B:
            return 1
    
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        if A[0][0] >B:
            return 0
        if A[-1][-1] < B:
            return 0
        # find row 
        row=0

        while True:
            if ( A[row][0] <= B )  and (B <= A[row][-1]):
                break
            row+=1
        # we are in correct row 
        return self.binaryserch(A[row],B,len(A[row]))
a=Solution()
A=[
    [5, 17, 100, 111],
    [119, 120,  127,   131] 
]
B = 130
# x=a.binaryserch([5,12,15,20],19,0,4)
x=a.searchMatrix(A,B)
print(x)