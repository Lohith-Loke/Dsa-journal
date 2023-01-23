''''
N children are standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum number of candies you must give?
'''

class Solution:
    def candy(self,A):
        n=[1]*len(A)
        i=1
        while i< len(A):
            if A[i] > A[i-1]:
                # incriment n[i] to be greater than n[i-1]
                while n[i-1]>=n[i]:
                    n[i]=1+n[i]
            i+=1
        i=len(A)-1

        while i>0:
            if A[i]<A[i-1]:
                while n[i-1]<=n[i]:
                    n[i-1]=1+n[i-1]
            i-=1

        return sum(n)

A = [1, 2, 2]
#A = [1, 3, 2, 1]
a=Solution()
x=a.candy(A)
print(x)