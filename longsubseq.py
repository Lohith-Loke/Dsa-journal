#!/usr/bin/env python3

txt2 = "kabc"
txt1 = "decdac"
dk={}
for i in range(len(txt2)):
    dk[txt2[i]]=i
curr=0
res=[]
for i in range(len(txt1)):
    if txt1[i] in dk:
        # in dictionary 
        if dk[txt1[i]]>curr:
            curr+=1
            # append this char
            res.append(txt1[i])

print(res) 