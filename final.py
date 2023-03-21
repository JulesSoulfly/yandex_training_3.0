# https://contest.yandex.ru/contest/46304/problems/A/
def a():
    stack = []
    stocks = {}
    with open('input.txt', 'r') as f:
        N = int(f.readline().strip())
        while True:
            l = f.readline()
            if not l: break
            l = l.split()
            if l[0] == 'add':
                n = int(l[1])
                if len(stack) > 0 and stack[-1][0] == l[2]:
                    stack[-1][1] += n
                else:
                    stack.append([l[2], n])
                if l[2] not in stocks:
                    stocks[l[2]] = 0
                stocks[l[2]] += n
            elif l[0] == 'delete':
                n = int(l[1])
                while len(stack) > 0 and stack[-1][1] <= n:
                    n -= stack[-1][1]
                    a, b = stack.pop()
                    stocks[a] -= b
                if len(stack) > 0:
                    stack[-1][1] -= n
                    stocks[stack[-1][0]] -= n
            elif l[0] == 'get':
                if l[1] not in stocks:
                    stocks[l[1]] = 0
                print(stocks[l[1]])


# don't closed
# https://contest.yandex.ru/contest/46304/problems/C/
def c():
    N = int(input())
    ans = []
    ac, bc = 0, 0
    a1, b1 = [int(x) for x in input().split()]
    a2, b2 = [int(x) for x in input().split()]
    if a <= b:
        ac += a
        ans.append('1')
    else:
        bc += b
        ans.append('2')
    for i in range(N-2):
        a, b = [int(x) for x in input().split()]
        if ac < bc:
            ac += a
            ans.append('1')
        else:
            bc += b
            ans.append('2')
    print(' '.join(ans))


# don't closed
# https://contest.yandex.ru/contest/46304/problems/E/
def e():
    H, W = [int(x) for x in input().split()]
    a, c = [], []
    for i in range(H):
        a.append([*input()])
        b = []
        for _ in range(W): b.append([-1,-1])
        c.append(b)
    sx, sy = [int(x)-1 for x in input().split()]
    tx, ty = [int(x)-1 for x in input().split()]
    a = a[::-1]
    def get(arr, coords):
        return arr[coords[1]][coords[0]]
    def set(arr, coords, val):
        arr[coords[1]][coords[0]] = val
    dirs = [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
    q = []
    q.append([sx, sy])
    set(c, [sx, sy], [0,9])
    while(len(q) > 0):
        el = q.pop(0)
        for i in range(8):
            dx, dy = dirs[i]
            x, y = el[0]+dx, el[1]+dy
            if x >= 0 and x < W and y >= 0 and y < H:
                cell = get(a, [x,y])
                if cell == '.':
                    cur = get(c, el)
                    cur = cur[:]
                    if cur[1] != i:
                        cur[0] += 1
                        cur[1] = i
                    val = get(c, [x,y])
                    if val == [-1,-1] or val[0] > cur[0]:
                        set(c, [x,y], cur)
                        q.append([x,y])
    ans = c[ty][tx][0]
    print(ans)
