# max area of histogram 
# largest rectangle in histogram
# Return the area of largest rectangle in the histogram.

class Solution:
    def left(self,A):
        stq=[]
        sol=[]
        i=len(A)-1
        lftmax=len(A) 
        while i >-1:
            if stq:
                while A[stq[-1]]>=A[i]:
                    stq.pop()
                    if not stq:
                        break
                if stq:
                    sol.append(stq[-1])
                else:
                    sol.append(lftmax)
            else:
                sol.append(lftmax)
            stq.append(i)
            i-=1
        sol.reverse()
        return sol

    def right(self,A):
        stq=[]
        sol=[]
        i=0
        rtmax=0
        while i<len(A):
            if stq:
                while A[stq[-1]]>=A[i]:
                    stq.pop()
                    if not stq:
                        break
                if stq:
                    sol.append(stq[-1]+1)
                else:
                    sol.append(rtmax)
            else:
                sol.append(rtmax)
            stq.append(i)
            i+=1
        return sol
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self,A):
        # right max =0 right idx =limit-1
        right=self.right(A)
        # left max = len(A) idx = limit
        left=self.left(A)
        print("Right:",right)
        print("left: ",left)
        Area=[]
        mx=-1000
        for i in range(len(A)):
            rl=right[i]
            ll=left[i]
            mx=max((ll-rl)*A[i],mx)
            Area.append((ll-rl)*A[i])
        print("Area: ",Area)
        print("mx:",mx)
A = [1,2,4]
ans= 10
# A = [2]
# ans=2 
a=Solution()

x=a.largestRectangleArea(A)