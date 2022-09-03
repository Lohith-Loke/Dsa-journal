import sys
A = [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0]
# A = [1, 1, 1, 1]
B = 12
# print(len(A))
# [ X-B+1, X+B-1].


class Solution:

    def solve(self, A, B):
        cur = B-1
        count = 0
        toend = False
        if B > len(A):
            cur = len(A)-1
            count = -1

        up = B-1
        low = 0

        while True:
            if A[cur] == 1:

                # new current = cur +B-1
                cur = min(cur+2*B-1, len(A)-1)
                up = min(cur+B-1, len(A)-1)
                low = max(0, cur-B+1)
                count += 1
                if up >= len(A)-1:
                    toend = True

            else:
                while True:
                    cur -= 1
                    if low > cur:
                        return(-1)

                    if A[cur] == 1:
                        break
            if toend:
                break
        return count


# A = [1, 1, 1, 1]
# B = 3
z = Solution()
res = z.solve(A, B)
print(res)
