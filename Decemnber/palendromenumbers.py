class Solution:
    def ispalendrome(self,num):
            z=num
            c=0 
            rev=0
            while z!=0:
                rem = z%10
                rev = rev*10 +rem
                z=z//10
                c+=1
            
            if num == rev :
                return True 
            else:
                return False

    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    
    def solve(self, A, B, C):
        # get all palendrome b/w A & B 
        lst=[]
        for i in range(A,B):
            if self.ispalendrome(i):
                lst.append(i)
        z=c=len(lst)
        # use sliging window do narrow down
        low= 0
        # print(lst)
        r=0                    
        low=0
        ans=0
        while r<len(lst):
            if lst[r]-lst[low]<=C:
                ans= max(ans,r-low+1)
                r+=1
            elif r==len(lst):
                break
            else:
                while low<len(lst) and lst[r]-lst[low]>C:
                    low+=1
        # sart with window width = 1 
        high= 0 
        low = 0 
        ans= 0 
        while high <len(lst):
            if lst[high]-lst[low]<=C:
                # when max diff is less than c 
                ans= max(ans,high-low+1)
                high+=1 
            
            elif high==len(lst):
                break
            else:
                while low<len(lst) and lst[high]-lst[low]>C:
                    low+=1
        return ans
s=Solution()
x=s.solve(80,110,10)
print(x)