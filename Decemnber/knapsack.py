class Solution:
    lst=[]
    def Knaps(self,idx,wt,val,W):
        # break criteria end when ----
        if idx==len(wt) or W==0:
            return 0
       
        # dp serch 
        if self.lst[idx][W]!=-1:
            return self.lst[idx]

        if wt[idx]<=W:
            self.lst[idx][W]=max(self.Knaps(idx+1,wt,val,W),(val[idx]+self.Knaps(idx+1,wt,val,W-wt[idx])))
            return self.lst[idx][W]
        else:
            # cant take the element 
            self.lst[idx][W]=self.Knaps(idx+1,wt,val,W)
            return  self.lst[idx][W]
    
    def knapsnak(self,wt,val,W):
        self.lst=[[-1 for i in range(W+1)]for j in range(len(wt)+1)]
        return self.Knaps(0,wt,val,W) 

W=40
val=[10,20,30,40]
wt= [30,10,40,20]
a=Solution()
x=a.knapsnak(wt,val,W)
print(x)