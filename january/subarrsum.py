class Solution:
    def subArraySum(self,A, n, s): 
        #Write your code here
        i=1
        j=0
        sm=A[i]+A[j]
        i+=1
        j+=1
        while i <len(A):
            if sm == s:
                return [j,i]
            else:
                # either sm> s or sm <s
                if sm > s:
                    sm-=A[j]
                    j+=1
                else:
                    sm+=A[i]
                    i+=1
        return [-1] 

    #   0  1  2  3  4  5  6   
arr = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
sm=15
a=Solution()
x=a.subArraySum(arr,len(arr),sm)
print(x)