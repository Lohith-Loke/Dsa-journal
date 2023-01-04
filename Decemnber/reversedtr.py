class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A=A.rstrip()
        st=A.split(" ")
        st.reverse()
        x=""
        # print(st) 
        for i in st:
            if i=="":
                continue
            x+= i+" "
        x=x.rstrip()
        
        return x
a=Solution()
x=a.solve('''
       fwbpudnbrozzifml osdt ulc jsx kxorifrhubk ouhsuhf sswz qfho dqmy sn myq igjgip iwfcqq                 
''')
print(x)