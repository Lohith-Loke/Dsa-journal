# Element with left side smaller and right side greater

class Solution:
	def findElement(self,arr):
		# see left and find max element parce right find min element 
		#     prv3,prv2,prv, cur,nxt,net1,nxt2
		#     max(prv3,prv2,prv) =< cur <= min(nxt,net1,nxt2)
		arr.copy()
		# R ---> L
		mx=[arr[0]]
		i=1
		while i <len(arr):
			if mx[-1]<arr[i]:
				mx.append(arr[i])
			else:
				mx.append(mx[-1])
			i+=1
		mn=[arr[-1]]
		i-=2
		while i>-1 :
			if mn[-1]>arr[i]:
				mn.append(arr[i])
			else:
				mn.append(mn[-1])
			i-=1
		mn.reverse()
		print(mx)
		print(mn)
		res=[]
		i=1 # skip 0th element given 
		while i<len(arr)-1: # skip last element given 
			if mx[i]<=mn[i]:
				res.append(arr[i])
			i+=1
		if not res:
			return -1
		return res
		
#User function Template for python3

def findElement( arr, n):
    for i in range(1,n-1):
        j = i-1
        k = i+1
        flag = True
        while j>=0:
            if arr[i] < arr[j]:
                flag = False
                break
            j-=1
        while flag and k<n:
            if arr[k] < arr[i]:
                flag = False
                break
            k+=1
        if flag:
            return arr[i]
    return -1
    
arr=[2,3,5]
# arr=[3 ,6, 4, 5, 9, 8, 7]
arr=[11, 9, 12] # no ans 
arr=[4, 2, 5, 7]
a=Solution()
x=a.findElement(arr)
print(x)