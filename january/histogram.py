class Solution(object):
    def ncsleft(self,arr):
        stk=[]
        res=[len(arr)]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            if stk:
                while arr[stk[-1]]>=arr[i]:
                    stk.pop()
                    if  not stk:
                        break
                if stk:
                    res[i]=stk[-1]
            stk.append(i)
        return res

    def  ncsright(self,arr):
        stk=[]
        res=[0]*len(arr)
        for i in range(len(arr)):
            if stk:
                while arr[stk[-1]]>=arr[i]:
                    stk.pop()
                    if not  stk:
                        break
                if stk:
                    res[i]=stk[-1]+1
            stk.append(i)
        return res

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        right=self.ncsright(heights)
        left =self.ncsleft(heights)
        print("right ",right)
        print("left  ",left )
        _mx=-1000
        for i, j,k in zip(left,right,heights):
            _mx= max((i-j)*k,k,_mx)
        return _mx
        
s=Solution()
x=s.largestRectangleArea([1,1])
print(x)