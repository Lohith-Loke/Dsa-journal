class Solution:
    def duplicates(self,arr):
        lst=[]
        for i in range(len(arr)):
            if arr[abs(arr[i])]<0:
                lst.append(abs(arr[i]))
            else:
                arr[abs(arr[i])]= arr[abs(arr[i])]*-1
        if not lst:
            lst.append(-1)
        return lst
a=Solution()
x=a.duplicates([2,3,1,2,3])
print(x)