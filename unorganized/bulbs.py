
e = [1, 0, 0, 0, 0, 0, 0, 0, 1]
f = 4
print(len(e))
for i in e:
    print(i, end=" ")
print()
for i in range(0, len(e)):
    print(i, end=" ")
print()


def solve(a, b):
    i = b-1
    c = 0
    prv = 0
    while i < len(a):
        print(i, "=", a[i])
        found = False
        if a[i] != 1:
            prv = 0
            print(prv, i)
            up = b-1-1
            while up>pr
                # print(j)
                if j >= len(a):
                    break
                if a[j] == 1:
                    print("found")
                    prv = j
                    i = j
                    found = True
                    break
            if not found:
                print(found)
                print(-1)
        prv = i
        i += i+b-1
        c += 1
    return c


x = solve(e, f)
print(x)
