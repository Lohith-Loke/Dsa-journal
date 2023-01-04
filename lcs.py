#!/usr/bin/env python
def matrix_print(matrix):
    print('dp matrix :')
    for i in matrix:
        print(i)


def lcs(text1: str, text2: str):

    n = len(text1)
    m = len(text2)

    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    matrix_print(dp)

    print('lcs solution :', dp[n][m])

    i = n
    j = m
    LCS = []
    while i != 0 and j != 0:
        # print(i, j)
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            LCS.append(text1[i - 1])
            i -= 1
            j -= 1
    LCS = "".join(reversed(LCS))

    print('lcs string :', LCS)


if __name__ == "__main__":
    s1 = input("enter string 1 :")
    s2 = input("enter string 2 :")

    lcs(s1, s2)