# def lcs(x,y):

#     if len(x)==0 or len(y)==0:
#         return 0
#     if x[-1]==y[-1]:
#         return 1+lcs(x[0:-1],y[0:-1])
#     else:
#         return max(lcs(x,y[0:-1]),lcs(x[0:-1],y))

def lcsdp(x,y,d,n,m):
    if len(x)==0 or len(y)==0:
        return 0
    if d[n][m]!=-1:
        return d[n][m]
    if x[-1]==y[-1]:
        d[n][m]=1+lcsdp(x[0:-1],y[0:-1],d,n,m-1)
        return d[n][m]
    else:
        d[n][m]=max(lcsdp(x,y[0:-1],d,n,m-1),lcsdp(x[0:-1],y,d,n-1,m))
        return d[n][m]

def dpLcs(x,y):
    # memoization aproach in dp 
    dp=[[-1 for i in range(len(y)+1)]for j in range(len(x)+1)] 
    
    return lcsdp(x,y,dp,len(x),len(y))


X = "AGGTABtdkytttttttttttttttttttttcghdhgdgfddxghvhvxgfsetsxfgcxgnfsresrsxdsytdy5sjsyd"
Y = "GXTXAYBykughgrtdsyrsfgdsgseestrdy5dstsdtsesatfshtrstdsarewarsutsuktuyd,jmhtngtdjytcexyteyyxyt"
x=dpLcs(X,Y)
print(x) 