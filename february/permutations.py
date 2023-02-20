
class Solution:
    def reccursive(self,A):
        res=[]
        if len(A)==1:
            return [A[:]]
        picked=-1
        for i in range(len(A)):
            picked = A.pop(0)
            perms= self.reccursive(A)

            for p in perms:
                p.append(picked)
            res.extend(perms)
            A.append(picked)
        return res

    def permutaions(self,A):
        return self.reccursive(A)


A=[1,2,3]

a=Solution()
sol=a.permutaions(A)
print(sol)