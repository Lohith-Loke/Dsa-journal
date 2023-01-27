
# next smallest element 
def nseright(arr):
    stk=[]
    res=[-1]*len(arr)
    for i in range(len(arr)):
        if stk:
            if arr[stk[-1]]<arr[i]:
                res[i]=stk[-1]
            else:
                while stk[-1] >arr[i]:
                    stk.pop()
                    if stk:
                        pass
                    else:
                        break
                if stk:
                    res[i]=stk[-1]
        stk.append(i)
    return res

def nseleft(arr):
    # ----->
    stk=[]
    res=[-1]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        if stk:
            if arr[stk[-1]]<arr[i]:
                res[i]=stk[-1]
            else:
                # need to pop look up stack
                while arr[stk[-1]]>arr[i]:
                    stk.pop()
                    if  stk:
                        # we have more elements
                        pass
                    else:
                        # no element present 
                        break
                if stk:
                    res[i] = stk[-1]
        stk.append(i)
    return res

arr= [11,13,21,3]
print(arr)
left= nse(arr)
right= nseright(arr)
print(left)
print(right)
