A = "1.13"
B = "1.13.4"
ans=-1

A = "1.13.99"
B = "1.13.99.00"
ans=0

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        first=A.split(".")
        second=B.split(".")
        i =0
        while True:
            if i==len(first):
                break
            if i ==len(second):
                break
            x=int(first[i])
            y=int(second[i])
            if x==y:
                i+=1
                continue
            if x>y:
                return 1
            else:
                return -1
        if len(first)!=len(second):
            if len(first)>len(second):
                
                while i<len(first):
                    x=int(first[i])
                    i+=1
                    if x==0:
                        continue
                    else:
                        return 1    
                # A = 1.0
                # B = 1 ans = 0
                return 0 
            else:
                while i <len(second):
                    y=int(second[i])
                    i+=1
                    if y==0:
                        continue
                    else:
                        return -1
                return 0
        return 0
a=Solution()
x=a.compareVersion(A,B)
print(x)