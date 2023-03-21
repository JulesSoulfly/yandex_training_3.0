from functools import lru_cache

# https://contest.yandex.ru/contest/45468/problems/31/
def e31():
    n, m = [int(x) for x in input().split()]
    g = [[] for _ in range(n+1)]
    c = set()
    c.add(1)
    for _ in range(m):
        e1, e2 = [int(x) for x in input().split()]
        g[e1].append(e2)
        g[e2].append(e1)
    v = [False for _ in range(n+1)]
    def dfs(i):
        v[i] = True
        for x in g[i]:
            if not v[x]:
                c.add(x)
                dfs(x)
    dfs(1)
    print(len(c))
    print(' '.join([str(x) for x in sorted(c)]))


# https://contest.yandex.ru/contest/45468/problems/32/
@lru_cache(maxsize=None)
def e32rec():
    import sys
    import threading
    threading.stack_size(67108864) # 64
    sys.setrecursionlimit(100000)
    def a():
        n, m = 0, 0
        c = [set()]
        c[0].add(1)
        ci = 0
        g = None
        with open('input.txt', 'r') as f:
            n, m = [int(x) for x in f.readline().split()]
            g = [[] for _ in range(n + 1)]
            while True:
                l = f.readline()
                if not l: break
                e1, e2 = [int(x) for x in l.split()]
                g[e1].append(e2)
                g[e2].append(e1)
        v = [False for _ in range(n+1)]
    #    [print(x) for x in g]
        def dfs(i):
            v[i] = True
            c[ci].add(i)
            for x in g[i]:
                if not v[x]: dfs(x)
        for i in range(1, n+1):
            if not v[i]:
                dfs(i)
                ci += 1
                c.append(set())
        if len(c[-1]) == 0: c.pop()
    #    print(ci)
        print(len(c))
        for i in range(ci):
            print(len(c[i]))
            print(' '.join([str(x) for x in c[i]]))
    thread = threading.Thread(target=a)
    thread.start()
    thread.join()


def e32():
    n, m = 0, 0
    c = [set()]
    c[0].add(1)
    ci = 0
    g = None
    with open('input.txt', 'r') as f:
        n, m = [int(x) for x in f.readline().split()]
        g = [[] for _ in range(n + 1)]
        while True:
            l = f.readline()
            if not l: break
            e1, e2 = [int(x) for x in l.split()]
            g[e1].append(e2)
            g[e2].append(e1)
    v = [False for _ in range(n+1)]
    st = []
    def dfs(i):
        st.append(i)
        while len(st) > 0:
            cur = st.pop()
            v[cur] = True
            c[ci].add(cur)
            for x in g[cur]:
                if not v[x]: st.append(x)
    for i in range(1, n+1):
        if not v[i]:
            dfs(i)
            ci += 1
            c.append(set())
    if len(c[-1]) == 0: c.pop()
#    print(ci)
    print(len(c))
    for i in range(ci):
        print(len(c[i]))
        print(' '.join([str(x) for x in c[i]]))


# https://contest.yandex.ru/contest/45468/problems/33/
def e33():
    n, m = 0, 0
    g = None
    with open('input.txt', 'r') as f:
        n, m = [int(x) for x in f.readline().split()]
        g = [[] for _ in range(n + 1)]
        while True:
            l = f.readline()
            if not l: break
            e1, e2 = [int(x) for x in l.split()]
            g[e1].append(e2)
            g[e2].append(e1)
    c = [0 for _ in range(n+1)]
    msg = "YES"
    colors = {1: 2, 2: 1}
    def dfs(i, color):
        c[i] = color
        for x in g[i]:
            if c[x] == color:
                return 1
            elif c[x] == 0:
                error = dfs(x, colors[color])
                if error: return error
    for i in range(1, n+1):
        if c[i] == 0:
            error = dfs(i, 1)
            if error:
                msg = "NO"
                break
    print(msg)


# https://contest.yandex.ru/contest/45468/problems/34/
def e34():
    n, m = 0, 0
    g = None
    with open('input.txt', 'r') as f:
        n, m = [int(x) for x in f.readline().split()]
        g = [[] for _ in range(n + 1)]
        while True:
            l = f.readline()
            if not l: break
            e1, e2 = [int(x) for x in l.split()]
            g[e1].append(e2)
    c = [0 for _ in range(n+1)]
    ans = []
    st = []
    def dfs(i, a):
        st.append([i, 0, 0])
        b = []
        while len(st) > 0:
            cur, prev, e = st.pop()
            c[cur] = 1
            while e < len(g[cur]):
                x = g[cur][e]
                if c[x] == 1: return 1
                elif x == prev or c[x] == 2:
                    e += 1
                    continue
                elif c[x] == 0:
                    st.append([cur, prev, e+1])
                    st.append([x, cur, 0])
                    break
            if e == len(g[cur]):
                c[cur] = 2
                ans.append(cur)
    cycle = None
    for i in range(1, n+1):
        if c[i] == 0:
            cycle = dfs(i, ans)
            if cycle:
                print(-1)
                break
    if not cycle:
        print(" ".join([str(x) for x in ans[::-1]]))


# https://contest.yandex.ru/contest/45468/problems/35/
def e35():
    n = 0
    g1 = None
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        g1 = []
        while True:
            l = f.readline()
            if not l: break
            g1.append([int(x) for x in l.split()])
    c = [0 for _ in range(n)]
    g = []
    for i in range(n):
        g.append([j for j in range(n) if g1[i][j] == 1])
    def dfs(i, prev, st):
        c[i] = 1
        st.append(i)
        for x in g[i]:
            if x == prev: continue
            elif c[x] == 1:
                while st[0] != x: st.pop(0)
                return 1
            elif c[x] == 0:
                cycle = dfs(x, i, st)
                if cycle: return cycle
        st.pop()
    cycle = None
    for i in range(n):
        if c[i] == 0:
            st = []
            cycle = dfs(i, -1, st)
            if cycle:
                print("YES")
                print(len(st))
                print(' '.join(str(x+1) for x in st[::-1]))
                break
    if not cycle: print("NO")
