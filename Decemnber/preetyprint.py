from turtle import pen


class Solution:
    def getnum(self,i):
        return 1+(i-1)*2
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        mx=[]
        lmx=self.getnum(A)
        for i in range(1,A+1):
            tmp=[i]*self.getnum(i)
            if len(tmp)<lmx:
                # need to add numbers
                while tmp[-1]!=A:
                    tmp.append(tmp[-1]+1)
                if len(tmp)<lmx:
                    # add the reverse of current list to tmp
                    x=lmx-len(tmp)
                    rev=tmp[::-1]
                    tmp=rev[:x]+tmp
                    pass 
            mx.append(tmp)
        mz=[]
        for i in range(len(mx)-1,0,-1):
            mz.append(mx[i])
        for i in mx:
            mz.append(i)
        for i in mz:
            for j in i:
                print(j,end=" ")
            print() 
        


s=Solution()
s.prettyPrint(20)