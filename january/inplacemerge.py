# Merge Without Extra Space
class Solution:    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        i = 0 
        j = 0
        k=0
        res= []
        while i <n and j <m:
            if arr1[i]<arr2[j]:
                res.append(arr1[i])
                i+=1
            else:
                res.append(arr2[j])
                j+=1
            
        while i<n:
            res.append(arr1[i])
            i+=1
        while j <m:
            res.append(arr2[j])
            j+=1
        
        for i in range(n):
            arr1[i]=res[i]

        for j in range(m):
            arr2[j]=res[i+j+1]

arr1= [1 ,3 ,5 ,7]
arr2 = [0,2,6,8,9]
a=Solution()
a.merge(arr1,arr2,len(arr1),len(arr2))
print(arr1,arr2)