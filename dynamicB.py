
# https://contest.yandex.ru/contest/45468/problems/21/
def e21():
    N = int(input())
    dp = [0] * (N + 2)
    dp[0], dp[1], dp[2] = 1, 2, 4
    for i in range(3, N+1):
        dp[i] = sum(dp[i-3:i])
    print(dp[N])


# https://contest.yandex.ru/contest/45468/problems/22/
def e22():
    N, k = [int(x) for x in input().split()]
    dp = [1] * (N + 2)
    for i in range(2, min(k, N)):
        dp[i] = sum(dp[:i])
    for i in range(k, N):
        dp[i] = sum(dp[i - k:i])
    print(dp[N-1])


# https://contest.yandex.ru/contest/45468/problems/23/
def e23():
    N = int(input())
    dp = [0] * (N+2)
    inf = 1000001
    ind = [0] * (N+2)
    if N > 1:
        for i in range(2, N+1):
            ind_x2, ind_x3, ind_p1 = i//2, i//3, i-1
            x2 = dp[ind_x2] + 1 if ind_x2 * 2 == i else inf
            x3 = dp[ind_x3] + 1 if ind_x3 * 3 == i else inf
            p1 = dp[ind_p1] + 1
            if x3 <= x2 and x3 <= p1:
                dp[i] = x3
                ind[i-1] = ind_x3
            elif x2 <= x3 and x2 <= p1:
                dp[i] = x2
                ind[i-1] = ind_x2
            else:
                dp[i] = p1
                ind[i-1] = ind_p1
        i = N-1
        inf = dp[N]
        dp.clear()
        while i > 0:
            dp.insert(0, str(ind[i]))
            i = ind[i] - 1
        dp.append(str(N))
    else:
        inf = 0
        dp = ['1']
    print(inf)
    print(' '.join(dp))



# https://contest.yandex.ru/contest/45468/problems/24/
def e24():
    N = int(input())
    a = [[float('inf'), float('inf'), float('inf')]]
    for _ in range(N):
        a.append([int(x) for x in input().split()])
    dp = [0] * (N+1)
    dp[0] = 0
    dp[1] = a[1][0]
    if N > 1:
        dp[2] = min(a[1][1], dp[1] + a[2][0])
        for i in range(3, N+1):
            dp[i] = min([a[i-2][2]+dp[i-3], a[i-1][1]+dp[i-2], a[i][0]+dp[i-1]])
    print(dp[N])


# https://contest.yandex.ru/contest/45468/problems/25/
def e25():
    N = int(input())
    a = sorted([int(x) for x in input().split()])
    dp = [str('inf')] * N
    dp[1] = a[1] - a[0]
    st = [0, 1]
    if N > 2:
        dp[2] = a[2] - a[0]
        for i in range(3, N):
            d = a[i] - a[i-1]
            dp[i] = min([dp[i-2] + d, dp[i-1] + d])
    print(dp[-1])

