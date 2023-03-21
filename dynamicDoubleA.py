# https://contest.yandex.ru/contest/45469/problems/27/
def e27():
    s1 = input()
    s2 = input()
    dp = [[x for x in range(len(s2)+1)]]
    for i in range(1, len(s1)+1): dp.append([i] + [0]*len(s2))
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            c = 1 if s1[i-1] != s2[j-1] else 0
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+c)
    print(dp[len(s1)][len(s2)])


# don't closed
# https://contest.yandex.ru/contest/45469/problems/30/
def e30():
    L, n = [int(x) for x in input().split()]
    a = [0] + [int(x) for x in input().split()] + [L]
    d = {}
    for i in range(1, n+1): d[(i-1,i+1)] = a[i+1] - a[i-1]
    print(d)
    for i in range(3, len(a)-1):
        for j in range(i, len(a)):
            print(i, j, a[j]-a[j-i])
            els = i-1
            aa = []
            for x in range(j-i, (j-i)+els):
                print('x:', x, 'els:', els)
                aa.append(d[(x,x+(i-1))])
#            [d[(x-(i-1),x)] for x in range(j, j-els, -1)]
            print('aa:', aa)
            d[(j-i,j)] = min(aa) + (a[j]-a[j-i])
            print(d)
    mn = float('inf')
    d[(0,1)] = 0
    d[(n,n+1)] = 0
    print(d)
    for i in range(1, n+1):
        print(d[(0,i)]+d[(i,n+1)]+L)
        mn = min(mn, d[(0,i)]+d[(i,n+1)]+L)
    print(mn)
