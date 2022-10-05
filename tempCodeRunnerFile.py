class Solution:
    #,@param,A,:,list,of,integers
    #,@return,an,integer
    def candy(self, A):
        d = {}
        for i in A:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        #,print(d)
        #,d,contains,freq,table,
        c = 0
        mn = 1
        b = list(d.keys())
        b.sort()
        for i in b:
            #,print(d[i],mn)
            c += d[i] * mn
            mn += 1
        print(c)
        return c