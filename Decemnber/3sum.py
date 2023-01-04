A = [-1, 2, 1, -4]
B = 1
ans= 2

# A = [1, 2, 3]
# B = 6
# ans=6

A=[5 ,-2 ,-1 ,-10 ,10]
B=5
ans= 5

A=[10, -6, 3, 4, -8, -5]
B=3
ans=2
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        # sort the array 
        A.sort()
        # use sliding window to get to closest sum 
        ans= 1000000000
        for i in range(len(A)):
            low = i+1 
            high =len(A)-1

            while high>low:
                sm=A[i]+A[low]+A[high]
                if sm==B:
                    return sm
                if abs(B-sm)<abs(B-ans):
                    ans=sm
                if abs(B-sm)==abs(B-ans):
                    ans=max(sm,ans)
                if sm>B:
                    # if sum >B reduce window by 1 
                    high-=1
                else:
                    # if sum < B  increase window by 1 
                    low+=1
        return ans
a=Solution()
x=a.threeSumClosest(A,B)
if x==ans:
    print("result correct ")
else:
    print(x,"incorrect ")