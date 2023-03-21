# https://contest.yandex.ru/contest/45468/problems/36/
def e36():
    N = int(input())
    g = [[]]
    for i in range(N):
        a = [int(x) for x in input().split()]
        g.append([i+1 for i, e in enumerate(a) if e == 1])
    v1, v2 = [int(x) for x in input().split()]
    p, q, c = [-1 for _ in range(N+1)], [], [-1 for _ in range(N+1)]
    if v1 == v2: print(0)
    else:
        def bfs(v):
            p[v] = 0
            q.append(v)
            c[v] = 0
            while len(q) > 0:
                el = q.pop(0)
                for x in g[el]:
                    if x == p[el] or c[x] != -1: continue
                    c[x] = c[el] + 1
                    q.append(x)
                    p[x] = el
                    if x == v2: return
        bfs(v1)
        if p[v2] == -1: print(-1)
        else:
            print(c[v2])
            b, i = [str(v2)], v2
            while i != v1:
                b.insert(0, str(p[i]))
                i = p[i]
            print(' '.join(b))


# https://contest.yandex.ru/contest/45468/problems/37/
def e37():
# look at e36
    pass


# https://contest.yandex.ru/contest/45468/problems/38/
def e38():
    N, M, S, T, Q = [int(x) for x in input().split()]
    a, b, q = [], [], []
    for _ in range(Q): b.append([int(x) for x in input().split()])
    for _ in range(N): a.append([-1] * M)
    q = []
    a[S-1][T-1] = 0
    q.append((S-1, T-1))
    while(len(q)) > 0:
        el = q.pop(0)
        for dx, dy in [(2,1), (-2,1), (2,-1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]:
            x, y = el[0] + dx, el[1] + dy
            if x >= 0 and x < N and y >= 0 and y < M and a[x][y] == -1:
                q.append((x,y))
                a[x][y] = a[el[0]][el[1]] + 1
    sm = 0
    for x, y in b:
        if a[x-1][y-1] == -1:
            print(-1)
            exit()
        sm += a[x-1][y-1]
    print(sm)


# https://contest.yandex.ru/contest/45468/problems/39/
def e39():
    N = int(input())
    a, c = [], []
    xyz = 0
    for i in range(N):
        input()
        a.append([])
        c.append([])
        for j in range(N):
            a[i].append([*input()])
            c[i].append([-1]*N)
            for z, x in enumerate(a[i][j]):
                if x == 'S': xyz = (i, j, z)
    def get(arr, coords):
        for coord in coords:
            arr = arr[coord]
        return arr
    def set(arr, coords, val):
        arr[coords[0]][coords[1]][coords[2]] = val
    q = []
    q.append(xyz)
    set(c, xyz, 0)
    while(len(q) > 0):
        el = q.pop(0)
        for dx, dy, dz in [(0,1,0),(1,0,0),(0,-1,0),(-1,0,0),(0,0,1),(0,0,-1)]:
            x, y, z = el[0]+dx, el[1]+dy, el[2]+dz
            if x >= 0 and x < N and y >= 0 and y < N and z >= 0 and z < N:
                if get(c, (x,y,z)) == -1:
                    cur = get(c, el) + 1
                    cell = get(a, (x,y,z))
                    if cell == '.':
                        if x == 0:
                            print(cur)
                            exit()
                        set(c, (x,y,z), cur)
                        q.append((x,y,z))


# https://contest.yandex.ru/contest/45468/problems/40/
def e40():
    N = int(input())
    M = int(input())
    v, p = [[]], [[]]
    for _ in range(N+1): v.append([])
    for i in range(1, M+1):
        P, *x = [int(x) for x in input().split()]
        p.append(x)
        for j in range(P): v[x[j]].append(i)
    A, B = [int(x) for x in input().split()]
    c, q = [-1] * (M+1), []
    g = []
    for _ in range(M+1): g.append(set())
    for x in v:
        for i in range(len(x)):
            for j in range(len(x)):
                if x[i] != x[j]: g[x[j]].add(x[i])
    for x in v[A]:
        c[x] = 0
        q.append(x)
    ans = -1
    while len(q) > 0:
        el = q.pop(0)
        if B in p[el]:
            ans = c[el]
            break
        else:
            for x in g[el]:
                if c[x] == -1:
                    c[x] = c[el] + 1
                    q.append(x)
    print(ans)
