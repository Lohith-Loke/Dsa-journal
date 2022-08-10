# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         d1 = {}
#         d2 = {}
#         for char in s:
#             if char in d1:
#                 d1[char] += 1 
#                 continue
#             d1[char] = 1
#         for char in t:
#             if char in d2:
#                 d2[char] += 1
#                 continue
#             d2[char] = 1
#         if d1 != d2:
#             return False
#         return True

class Solution:
    # @param A : string
    # @param B : list of list of integers
    # @return a list of list of integers
    # find subarray of A with whose A xor B[i][0]= B[i][1] return [starting index ,ending index] return [-1,-1] if not found
    def substring(self,A):
        l= len(A)
        result=[]
        for i in range(l):
            for j in range(i,l):
                result.append(A[i:j+1])
        return result
        
    def solve(self, A,B):
        l= len(A)
        result=[]
        substr=self.substring(A)
        for i in substr:
            # if i xor B[i][0]==B[i][1] append 
            if self.xor(i,B[0][0])==B[0][1]:
                result.append(i)

a = Solution()
print(a.getAllSubArray("10"))
