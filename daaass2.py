# 
import collections
from turtle import st
a=[2,1,5,2]
# a=[2,1,5]
stack=collections.deque([0])
leftlimit=[0]

for i in range(1,len(a)):
    if a[i]<a[stack[0]]:
        # a[i] is smaller pop current head and check if its still true 
        stack.pop()
        stack.appendleft(i)
        if stack:
            pass
        leftlimit.append(i-1)
        # while stack:
        #     # run till stack is empty 
        #     if a[i]<a[stack[0]]:
        #         # we found a limiting value 
        #         break 
        # pass

print(leftlimit)
print(stack)