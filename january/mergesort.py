def mergesort(arr):
    if len(arr)<=1:
        return 0
    mid = len(arr)//2
    left_sub= arr[:mid]
    right_sub= arr[mid:]
    invercount=0
    invercount+= mergesort(right_sub)
    invercount+= mergesort(left_sub)
    i = 0 
    j = 0
    k = 0 
    while i <len(left_sub) and j<len(right_sub):
        if left_sub[i]<=right_sub[j]:
            # if i<mid+j:
                # invercount+= mid-i 
            arr[k]= left_sub[i]
            i+=1

        else:
            invercount+= mid-i
            arr[k]= right_sub[j]
            j+=1
        
        k+=1
    while i<len(left_sub):
        arr[k]=left_sub[i]
        i+=1
        k+=1
    while j<len(right_sub):
        arr[k]=right_sub[j]
        j+=1
        k+=1

    return invercount

arr=[2, 4, 1, 3, 5]

arr=[-2,3,-5]
arr=[-1,2,-8,-10]
print(arr)
ic=mergesort(arr)
print(arr)
print(ic)