class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def mergewithtemp(self, A, B):
        lna=len(A)
        lnb=len(B)
        res=[]
        i = 0
        j = 0 
        while True:
            if i ==lna:
                while j <lnb:
                    res.append(B[j])
                    j+=1
                break
            if j ==lnb:
                while i <lna:
                    res.append(A[i])
                    i+=1
                break
            if A[i] >B[j]:
                # add b  to res
                res.append(B[j])
                j+=1
            else:
                res.append(A[i])
                i+=1
        return res
    def getidx(A,ele,ptr):
        
        while ptr<len(A):
            if ele < A[ptr]:
                break
            prt+=1
        # position to insert 
        return ptr


    def merge(self, A, B):
        lna=len(A)
        lnb=len(B)
        i = 0
        j = 0 
        while True:
            if i ==lna:
                while j <lnb:
                    A.append(B[j])
                    j+=1
                break
            if A[i]>B[j]:
                # B[j] should be in A[i] position 
                tmp=A[i]
                A[i]=B[j]
                k=j+1
                while k!=lnb:
                    if B[k]>tmp:
                        
                        break
                    k+=1
                if k == lnb:
                    B.append(tmp)
                    j+=1
                    lnb+=1
                i+=1
            else:
                # A [i] is in correct position 
                i+=1
        

A=[-4,3]
B=[-2,-2,7]
# A.sort()
# B.sort()
# print(A)
# print(B)
a=Solution()
res=a.merge(A,B)
print(res)

