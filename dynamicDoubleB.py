
# https://contest.yandex.ru/contest/45468/problems/26/
def e26():
    n, m = [int(x) for x in input().split()]
    inf = float('inf')
    a = []
    for i in range(n):
        a.append([inf] + [int(x) for x in input().split()])
    for i in range(2, m+1): a[0][i] = a[0][i-1] + a[0][i]
    for i in range(1, n):
        for j in range(1, m+1): a[i][j] = min(a[i-1][j]+a[i][j], a[i][j-1]+a[i][j])
    print(a[n-1][m])


# https://contest.yandex.ru/contest/45468/problems/27/
def e27():
    n, m = [int(x) for x in input().split()]
    a, b = [], []
    for i in range(n):
        a.append([-1] + [int(x) for x in input().split()])
        b.append(['D']*(m+1))
    for i in range(2, m+1):
        a[0][i] = a[0][i-1] + a[0][i]
        b[0][i] = 'R'
    for i in range(1, n):
        for j in range(1, m+1):
            if a[i-1][j] + a[i][j] > a[i][j-1] + a[i][j]: a[i][j] = a[i-1][j] + a[i][j]
            else:
                a[i][j] = a[i][j-1] + a[i][j]
                b[i][j] = 'R'
    c, i, j = [], n-1, m
    while i >= 0 and j > 0:
        if i == 0 and j == 1: break
        cc = b[i][j]
        c.append(cc)
        if cc == 'D': i -= 1
        else: j -= 1
    print(a[n-1][m])
    print(' '.join(c[::-1]))


# https://contest.yandex.ru/contest/45468/problems/28/
def e28():
    n, m = [int(x) for x in input().split()]
    dp = []
    for _ in range(n): dp.append([-1]*m)
    dp[0][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            d1 = dp[i-2][j-1] if i-2 >=0 and j-1 >= 0 else -1
            d2 = dp[i-1][j-2] if i-1 >=0 and j-2 >= 0 else -1
            if d1 == -1 and d2 == -1: dp[i][j] = -1
            elif d1 == -1: dp[i][j] = d2
            elif d2 == -1: dp[i][j] = d1
            else: dp[i][j] = d1 + d2
    if dp[n-1][m-1] == -1: dp[n-1][m-1] = 0
    print(dp[n-1][m-1])



# https://contest.yandex.ru/contest/45468/problems/29/
def e29():
    n = int(input()) + 1
    a, m, inf = [0], n + 2, float('inf')
    dp = [[inf] * (m)]
    for _ in range(n-1):
        a.append(int(input()))
        dp.append([inf] * (m))
    dp[0][1] = 0
    for i in range(1, n):
        get = a[i] > 100
        if get: dp[i][1] = dp[i-1][2]
        else: dp[i][1] = min(dp[i-1][2], dp[i-1][1] + a[i])
        for j in range(2, m-1):
            if get: dp[i][j] = min(dp[i-1][j+1], dp[i-1][j-1] + a[i])
            else: dp[i][j] = min(dp[i-1][j+1], dp[i-1][j] + a[i])
#    [print(x) for x in dp]
    mn, mni, b = inf, 0, []
    for i in range(m-1, -1, -1):
        if dp[n-1][i] < mn: mn, mni = dp[n-1][i], i
    print(mn)
    print(mni-1, end = ' ')
    for i in range(n-1, 0, -1):
        x = dp[i][mni]
        if x == dp[i-1][mni+1]:
            b.append(str(i))
            mni += 1
        elif a[i] > 100: mni -= 1
    print(len(b))
    print('\n'.join(b[::-1]))


# https://contest.yandex.ru/contest/45468/problems/30/
def e30():
    n1 = int(input()) + 1
    s1 = [int(x) for x in input().split()]
    n2 = int(input()) + 1
    s2 = [int(x) for x in input().split()]
    dp, b = [], []
    for _ in range(n1): dp.append([0] * n2)
    for i in range(1, n1):
        for j in range(1, n2):
            if s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    i, j = n1-1, n2-1
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            b.append(str(s1[i-1]))
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i][j-1]: j -= 1
            else: i -= 1
#    print(dp[n1-1][n2-1])
    print(' '.join(b[::-1]))