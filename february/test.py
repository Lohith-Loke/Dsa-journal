from functools import cmp_to_key

arr=[3,30,34,5,9]

def cmp_items(a, b):
    if a[0] > b[0]:
        if a>b:
            return -1
        else:
            return 1
    elif a[0] == b[0]:
        if int(a+b)>int(b+a):
            return -1
        return 1
    else:
        if a>b:
            return 1
        else:
            return -1
        

cmp_items_py3 = cmp_to_key(cmp_items)
for i in range(len(arr)):
    arr[i]=str(arr[i])
arr.sort(key=cmp_items_py3)
res= "".join(i for i in arr )
print(res)
print("9534330")