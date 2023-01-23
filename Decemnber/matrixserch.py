class Solution:
    ## recursive approach 
    def binary(self,A,B,high,low):
        mid=(high+low)//2
        if (high < low):
            return 0 
        if  A[mid] < B:
            ## ele is b/w mid and high 
            return self.binary(A,B,high,mid+1)            
        if  A[mid] > B:
            ## ele is b/w low and mid 
            return self.binary(A,B,mid-1,low)
        if A[mid]==B:
            return 1 
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        if A[0][0]>B:
            ## less than 0,0 ele 
            return 0 
        if A[-1][-1]<B:
            # greater than last,last ele 
            return 0 
        row =0 
        while True:
            if A[row][0] <= B and A[row][-1] >= B:
                break
            row+=1
            
        return self.binaryserch(A[row],B,len(A[row]),0)
s=Solution()
A=   [ [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]  ]
B = 59
x=s.searchMatrix(A,B)
print(x)