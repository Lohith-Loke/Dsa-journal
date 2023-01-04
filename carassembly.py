#!/usr/bin/env python
def carAssembly(a, t, e, x):
    path = []
    NUM_STATION = len(a[0])
    T1 = [0 for i in range(NUM_STATION)]
    T2 = [0 for i in range(NUM_STATION)]

    T1[0] = e[0] + a[0][0]  # time taken to leave

    T2[0] = e[1] + a[1][0]  # time taken to leave

    if T1[0] < T2[0]:
        path.append(a[0][0])
    else:
        path.append(a[1][0])

    l1 = l2 = 0
    line1 = []
    line2 = []
    for i in range(1, NUM_STATION):
        inline = T1[i - 1] + a[0][i]
        skipto2 = T2[i - 1] + t[1][i] + a[0][i]
        l1 = a[0][i]
        if inline < skipto2:
            line1.append(1)
            T1[i] = inline
        else:
            line1.append(2)
            T1[i] = skipto2

        inline = T2[i - 1] + a[1][i]
        skipto2 = T1[i - 1] + t[0][i] + a[1][i]
        l2 = a[1][i]
        if inline < skipto2:
            line2.append(2)
            T2[i] = inline
        else:
            line2.append(1)
            T2[i] = skipto2

        if T1[i] < T2[i]:
            path.append(l1)
        else:
            path.append(l2)

    print(f'assembly line 1 cost :{T1}')
    print(f'path taken to achieve min cost {line1}\n\n')

    print(f'assembly line 2 cost :{T2}')
    print(f'path taken to achieve min cost {line2}\n\n')

    print(f'path taken for minimum cost {path}')
    # consider exit times and return minimum
    sol = min(T1[NUM_STATION - 1] + x[0], T2[NUM_STATION - 1] + x[1])
    #path traced
    print(f'minimum cost of assembly :{sol}')
    return sol

# cost of each stage a[0] lane 1 a[1] lane2
a = [[7, 9, 3, 4, 8, 4], [8, 5, 6, 4, 5, 7]]
# cost of each tarnsfer t[0] lane 1 t[1] lane2
t = [[0, 2, 3, 1, 3, 4], [0, 2, 1, 2, 2, 1]]
# entrence cost
e = [2, 4]
# exit cost
x = [3, 2]

carAssembly(a,t,e,x)
