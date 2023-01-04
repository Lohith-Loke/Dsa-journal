
class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        if B==1:
            return A
        lst=[ [] for i in range(B)]
        c=0
        up= True
        down=False
        for i in range(len(A)):
            print(A[i],end="->")
            print(c)
            lst[c].append(A[i])
            if down:
                c-=1
                if c==0:
                    down=False
                    up=True
                    continue
            if up:
                c+=1
                if c==B-1:

                    up=False
                    down=True
                    continue

        st=""
        for i in lst:
            for j in i:
                st+=j
        return st

A="kHAlbLzY8Dr4zR0eeLwvoRFg9r23Y3hEujEqdio0ctLh4jZ1izwLh70R7SAkFsXlZ8UlghCL95yezo5hBxQJ1Td6qFb3jpFrMj8pdvP6M6k7IaXkq21XhpmGNwl7tBe86eZasMW2BGhnqF6gPb1YjCTexgCurS"
B=1

a=Solution()
x=a.convert(A,B)
print(x)