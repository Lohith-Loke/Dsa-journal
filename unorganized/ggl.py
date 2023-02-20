

class Solution():
    def max_area(self, rec, maxarr=-1):
        b = 10000
        index = -1
        for i in range(len(rec)):
            if b > rec[i]:
                b = rec[i]
                index = i
        # we have min and its index
        area = b*len(rec)
        maxarr = max(area, maxarr)
        p1 = rec[index+1:]
        p2 = rec[:index]
        if p1:
            maxarr = self.max_area(p1, maxarr)
        if p2:
            maxarr = self.max_area(p2, maxarr)

        return maxarr


a = [
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]


# second half b[i+1:]
# first half b[i+1:]
# %%

rect = []
for i in range(len(a)):
    l = []
    for j in range(len(a[i])):
        temp = []
        for k in range(i):
            # print(a[k][j], end=" ")
            temp.append(a[k][j])
        if a[i][j] != 0:
            l.append(sum(temp)+a[i][j])
        else:
            l.append(a[i][j])
    print()
    rect.append(l)

m = -1
z = Solution()
for i in rect:
    # print(max(m, z.max_area(i)))
    m = max(m, z.max_area(i))

print(m)


# %%
