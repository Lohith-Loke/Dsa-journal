import string
A = 'scaler6~academy7~'
ans=['scaler', 'academy']
A="mxxxzclaql10~omttepvukq10~sckhqgagqt10~miaufqvumh10~jndrqnllah10~wqlithzmfi10~oczafaqcrz10~lnubllvcsq10~rzngzhllmw10~ntpvbeyxnk10~"

# A = 'interviewbit12~'
# ans=['interviewbit']

class Solution:
    # @param A : string
    # @return a list of strings
    def deserialize(self, A):
        res=[]
        i=0
        st=""
        while i<len(A):
            if A[i].isdigit():
                j = i
                while A[j].isdigit():
                    j+=1
                # we have all digits 
                i = j+1
                res.append(st)
                st=""
                continue
            st+=A[i]
            i+=1
        return res

a=Solution()
x=a.deserialize(A)
print(x)
# if x==ans:
#     print("result correct ")
# else:
#     print(x,"incorrect ")
