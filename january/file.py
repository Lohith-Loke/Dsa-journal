def printNGE(arr):
	st=[]
	res=[-1]*len(arr)
	for i in range(len(arr)):
		while st and arr[st[-1]]<arr[i]:
			res[st[-1]]=arr[i]
			st.pop()
		st.append(i)
	return res

# Driver code
arr = [7,8,1,4]
print(printNGE(arr))
