# 00 01 02
# 10 11 12
# 20 21 22
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        # digonal flip
        l = len(A)
        if l != len(A[0]):
            return False

        x, y = 0, l-1

        lst = []
        while True:
            if x < l and y > -1:
                lst.append(A[x][y])
                x += 1
                y -= 1
            else:
                break
        lst.reverse()
        i = 0
        x, y = 0, l-1
        while True:
            if x < l and y > -1:
                A[x][y] = lst[i]
                i += 1
                x += 1
                y -= 1
            else:
                break
        lst = []
        x, y = 0, 0
        while True:
            if x > l and y > l:
                lst.append(A[x][y])
                x += 1
                y += 1
            else:
                break
        lst.reverse()
        x, y = 0, 0
        while True:
            if x > l and y > l:
                A[x][y] = lst[i]
                x += 1
                y += 1
                i += 1
            else:
                break

        for i in A:
            print(i)
        return A


a = [[0, 0, 1, 0, 1, 0, 0, 1, 1, 1],
     [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
     [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
     [1, 1, 0, 0, 1, 0, 1, 1, 1, 0],
     [0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
     [1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
     [1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
     [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
     ]
b = [[0, 0, 0, 1, 0, 1, 1, 1, 1, 0]
     [0, 1, 1, 1, 1, 0, 1, 0, 0, 0]
     [1, 1, 1, 0, 1, 0, 1, 0, 0, 0]
     [0, 0, 1, 0, 1, 0, 0, 1, 1, 1]
     [1, 0, 1, 1, 1, 0, 1, 1, 1, 1]
     [0, 1, 1, 0, 0, 0, 0, 0, 1, 1]
     [0, 1, 0, 1, 1, 0, 0, 1, 1, 0]
     [1, 0, 1, 1, 1, 1, 0, 0, 1, 1]
     [1, 0, 0, 1, 0, 1, 1, 1, 1, 0]
     [1, 0, 1, 0, 0, 0, 0, 1, 1, 0]]

# print(a[0][1])
s = Solution()
s.solve(a)
