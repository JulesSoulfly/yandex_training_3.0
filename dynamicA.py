
# https://contest.yandex.ru/contest/45469/problems/21/
def e21():
    N = int(input())
    b = [x**3 for x in range(101)]
    inf = float('inf')
    for i in range(1, len(b)):
        if b[i] == N:
            print(1)
            exit()
    dp = [inf] * (N+1)
    dp[1] = 1
    for i in range(1, N+1):
        for j in range(1, len(b)):
            if b[j] > i: break
            rest = i - b[j]
            if rest == 0:
                dp[i] = 1
                break
            else: dp[i] = min(dp[i], dp[rest] + 1)
    print(dp[N])


# https://contest.yandex.ru/contest/45469/problems/22/
def e22():
    N = int(input())
    a = [int(x) for x in input().split()]
    dp = [0] * (N+1)
    dp[1] = 1
    indexes = [-1] * (N+1)
    M, I = 0, -1
    for i in range(2, N+1):
        m, ind = 0, -1
        for j in range(1, i):
            if a[i-1] > a[j-1] and m < dp[j]:
                m, ind = dp[j], j
        m += 1
        dp[i] = m
        indexes[i] = ind
        if m > M: M, I = m, i
    b = []
    while I > 0:
        b.append(str(a[I-1]))
        I = indexes[I]
    print(' '.join(b[::-1]))



# https://contest.yandex.ru/contest/45469/problems/23/
def e23():
    N = int(input())
    dp = [0] * (N+3)
    dp[1] = 1
    dp[2] = 5
    b1, b2, d, last = 2, 0, 0, 5
    for i in range(3, N+1):
        dp[i] = dp[i-1] + last + b1 + b2 + 1
        b1 += i
        d += 1 if i % 2 == 1 else 0
        b2 += d
        last += 2
    print(dp[N])


# https://contest.yandex.ru/contest/45469/problems/25/
def e25():
    n, a, b = [int(x) for x in input().split()]
    if a > b: a, b = b, a
    dp = [0] * (n+1)
    dp[0] = dp[1] = 0
    for i in range(2, n+1):
        dp[i] = min([max(dp[i-j]+b, dp[j]+a) for j in range(1, i)])
    print(dp)
    print(dp[n])