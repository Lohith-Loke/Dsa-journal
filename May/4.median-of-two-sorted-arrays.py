from typing import List
#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start


class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        # b - > bigger 
        
        if len(B)<len(A):
            A,B=B,A
        tot= len(A)+len(B)
        half=tot//2 # -> tot number of elements to be sorted 
        l,r= 0,len(A)-1
        while True:
            i= (l+r)//2
            j=half- i- 2 # array index issue 
            
            Aleft= A[i] if i >=0 else float("-infinity")
            Bleft= B[j] if j >=0 else float("-infinity")

            Aright=A[i+1] if (i+1)<len(A) else float("infinity")
            Bright=B[j+1] if (j+1)<len(B) else float("infinity")
            
            if Aleft<=Bright and Bleft<=Aright:
                if tot%2!=0:
                    return min(Aright,Bright)
                return (max(Aleft,Bleft)+min(Aright,Bright))/2
            
            elif Aleft >Bright:
                r=i-1
            else:
                l=i+1
        return 
        # merge num1 and num2  O(m+n) complexcity 
        

# @lc code=end
a=[1,3]
b=[2]

z=Solution()
x=z.findMedianSortedArrays(a,b)
print(x)