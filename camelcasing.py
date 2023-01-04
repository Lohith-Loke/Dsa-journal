res=[]
st="S;M;plasticCup()"
# Enter your code here. Read input from STDIN. Print output to STDOUT
from curses.ascii import isupper
import string 

# st=input()
split=""
op1,op2,data=st.split(";")
if op1=='S':
    # split
    split=" "
    pass
if op1=='C':
    # combine  
    split=""
    pass

    
if op2=='M':
    # method
    if st[len(st)-2]=='(':
        # remove () 
        st=st[0:len(st)-2]
    for i in st:
        if i.isupper():
            res.append(i.lower())
            continue
        res.append(i)
    
if op2=='V':
    # variable
    pass 

if op2=='C':
    pass

            
print(st)
a = [[7, 6, 7, 2], [2, 10, 1, 4]]
t = [[0, 7, 4, 5], [0, 9, 8, 2]]
e = [10, 12]
x = [18, 7]