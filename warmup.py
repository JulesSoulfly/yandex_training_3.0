
# https://contest.yandex.ru/contest/45468/problems/1/
def e1():
    s = []
    with open('input.txt', 'r') as f:
        s = f.readlines()
    s = ''.join(s)
    a = {}
    for c in s:
        if c not in a:
            a[c] = 0
        a[c] += 1
    if ' ' in a: del a[' ']
    if '\n' in a: del a['\n']
    keys = sorted(a)
    mx = max(a.values())
    for m in range(mx, 0, -1):
        l = []
        for k in keys:
            n = a[k]
            l.append(' ' if n < m else '#')
        print(''.join(l))
    print(''.join(keys))


# https://contest.yandex.ru/contest/45468/problems/2/
def e2():
    K = int(input())
    s = input().strip()
    if K >= len(s):
        print(len(s), end='')
    else:
        a = {chr(k):[] for k in range(ord('a'), ord('z')+1)}
        prev = s[0]
        start_index, r, beauty, i = 0, 1, 1, 1
        while i < len(s):
            if prev == s[i]: r += 1
            else:
                a[prev].append((start_index, r))
                beauty = max(beauty, r + K)
                prev = s[i]
                start_index, r = i, 1
            i += 1
        a[prev].append((start_index, r))
        beauty = max(beauty, r + K)
        beauty = min(len(s), beauty)
        for key in a:
            indexes = a[key]
            if len(indexes) > 1:
                iL, iR, k, acum, left_dist = 0, 1, K, indexes[0][1], 0
                while iL < len(indexes)-1 and iR < len(indexes):
                    L, R = indexes[iL], indexes[iR]
                    new_dist = R[0] - (indexes[iR-1][0] + indexes[iR-1][1])
                    if new_dist > K:
                        beauty = max(beauty, acum + k)
                        iL, k, acum = iR, K, R[1]
                    elif new_dist > k:
                        beauty = max(beauty, acum + k)
                        iL, k, acum = iL+1, k + left_dist, acum - L[1] - left_dist
                    elif new_dist < k:
                        iR, k, acum = iR+1, k - new_dist, acum + new_dist + R[1]
                    elif new_dist == k:
                        acum += new_dist + R[1]
                        beauty = max(beauty, acum)
                        k = k if iR - iL == 1 else k - new_dist + left_dist
                        iL, iR, acum, = iL+1, iR+1, acum - L[1] - left_dist
                    if iR == iL: iR += 1
                    if iR - iL == 1:
                        left_dist = 0
                        acum = indexes[iL][1]
                    elif iL < len(indexes)-1: left_dist = indexes[iL + 1][0] - (indexes[iL][0] + indexes[iL][1])
                beauty = max(beauty, acum + k)
        beauty = min(len(s), beauty)
        print(beauty, end='')

def e2n2():
    K = int(input())
    s = input().strip()
    if K >= len(s):
        print(len(s), end='')
    else:
        a = {chr(k):[] for k in range(ord('a'), ord('z')+1)}
        beauty = [0]
        for i in range(len(s)-1):
            r, k = 1, K
            for j in range(i+1, len(s)):
                if s[i] != s[j]:
                    k -= 1
                    r += 1
                    if k == 0: beauty = beauty if beauty[0] > r else [r, s[i], i, j]
                else: r += 1
        print(beauty)


# https://contest.yandex.ru/contest/45468/problems/3/
def e3():
    def bin(a, x):
        l, r, m = 0, len(a), 0
        while l < r:
            if a[m] < x: l = m + 1
            else: r = m
            m = (l + r) // 2
        return m

    n = int(input())
    d = sorted(set([int(x) for x in input().split()]))
    k = int(input())
    kn = [int(x) for x in input().split()]
    b = []
    for x in kn:
        i = bin(d, x)
        b.append(str(i))
    print('\n'.join(b), end = '')


# https://contest.yandex.ru/contest/45468/problems/4/
def e4():
    def calcseat(seat):
        return (seat // 2 + seat % 2, 2 - seat % 2)
    n, k, r, m = [int(input()) for _ in range(4)]
    maxr = n // 2 + n % 2
    seatP = r * 2 - (2 - m)
    seat1 = seatP - k
    seat2 = seatP + k
    if (seat1 < 1 and seat2 > n):
        print(-1)
    else:
        p1, m1 = calcseat(seat1)
        p2, m2 = calcseat(seat2)
        if p2 - r <= r - p1 and not seat2 > n: print(p2, m2)
        else: print(p1, m1)


# https://contest.yandex.ru/contest/45468/problems/5/
def e5():
    def find_min(l):
        if len(l) <= 1: return -1
        mini = 0
        for i in range(1, len(l)):
            if l[mini] >= l[i]: mini = i
        return mini

    def calc(l):
        if not l or len(l) <= 1: return 0
        intervals = [-1]
        for i in range(len(l)):
            if l[i] <= 0: intervals.append(i)
        intervals.append(len(l))
        s = 0
        for i in range(len(intervals)-1):
            newl = l[intervals[i]+1:intervals[i+1]]
            ind = find_min(newl)
            if ind != -1:
                n = newl[ind]
                s += (len(newl) - 1) * n
                L, R = [x-n for x in newl[0:ind]], [x-n for x in newl[ind+1:]]
                s += calc(L)
                s += calc(R)
        return s

    n = int(input())
    a = [int(input()) for x in range(n)]
    print(calc(a))


# https://contest.yandex.ru/contest/45468/problems/6/
def e6():
    m = int(input()) # не используется
    n = int(input())
    # тут храним сегменты, которые вручную сортируем при добавлении,
    # удаляя те старые, которые с новым пересекаются
    l = []
    for i in range(n): # читаем последовательно каждый сектор
        a, b = [int(x) for x in input().split()]
        # индекс, который будем двигать пока не найдём место для вставки
        j = 0
        # до тех пор пока оба конца элемента по индексу j
        # меньше начала нового сегмента, увеличиваем j (и проверяем не вышли ли за пределы списка)
        # вставим (7,11) в (1,2) (4,5), (8,9), (10,11), (100,100)
        # оба конца нулевого элемента (1,2) меньше чем 7, увеличили j (j=1)
        # (4,5) меньше 7, j=2
        # (8,9) - условие цикла нарушилось (7 меньше 8), выходим,
        # при этом j осталось равно 2 - мы нашли место для нового элемента
        while j < len(l) and (a > l[j][0] and a > l[j][1]): j += 1
        # найдя место проверяем все элементы по этому индексу на пересечение
        # формула пересечения двух отрезков:
        # x2 <= x1 <= y2   or   x2 <= y1 <= y2   or   x1 <= x2 <= y1   or   x1 <= y2 <= y1
        # x1 --------- y1
        #       x2 ---------- y2
        # (7,11) пересекается с (8,9) по индексу j=2, удаляем последний, индекс не двигаем
        # (7,11) пересекается с (10,11) по индексу j=2, удаляем последний, индекс не двигаем
        # (100,100) по индексу j=2 - нет пересечения, break
        while j < len(l):
            e = l[j]
            if (a >= e[0] and a <= e[1]) or (b >= e[0] and b <= e[1]) or (e[0] >= a and e[0] <= b) or (e[1] >= a and e[1] <= b):
                l.pop(j)
            else: break
        # наконец добавляем новый элемент по индексу j=2
        l.insert(j, (a, b))
    print(len(l))


# https://contest.yandex.ru/contest/45468/problems/7/
def e7():
    c = 24 * 3600 # + 59 * 60 + 59
    def convert_to(t):
        return int(t[2]) + int(t[1]) * 60 + int(t[0]) * 3600
    def convert_from(t):
        if t >= c: t -= c
        h = t // 3600
        d = t % 3600
        m = d // 60
        s = d % 60
        return ':'.join([str(x).zfill(2) for x in [h, m, s]])
    t1 = convert_to(input().split(':'))
    t2 = convert_to(input().split(':'))
    t3 = convert_to(input().split(':'))
    if t3 < t1: t3 += c
    d = t3 - t1
    d = d // 2 + d % 2
    t2 += d
    print(convert_from(t2))


# https://contest.yandex.ru/contest/45468/problems/8/
def e8():
    n = int(input())
    minx, miny = [int(x) for x in input().split()]
    maxx, maxy = minx, miny
    for i in range(1, n):
        x, y = [int(x) for x in input().split()]
        minx = min(x, minx)
        miny = min(y, miny)
        maxx = max(x, maxx)
        maxy = max(y, maxy)
    print(minx, miny, maxx, maxy)


# https://contest.yandex.ru/contest/45468/problems/9/
def e9():
    n, m, k = [int(x) for x in input().split()]
    a = [[0 for _ in range(m+1)]]
    for i in range(1, n+1):
        a.append([0] + [int(x) for x in input().split()])
    for i in range(1, n+1):
        for j in range(1, m+1): a[i][j] = a[i-1][j] + a[i][j-1] - a[i-1][j-1] + a[i][j]
    b = []
    for _ in range(k):
        x1, y1, x2, y2 = [int(x) for x in input().split()]
        b.append(str(a[x2][y2] - a[x2][y1 - 1] - a[x1 - 1][y2] + a[x1 - 1][y1 - 1]))
    print('\n'.join(b), end = '')


# https://contest.yandex.ru/contest/45468/problems/10/
def e10():
    s = input()
    n = len(s)
    d = {}
    for i in range(n):
        c = s[i]
        sum = (n - i) * (i + 1)
        if c not in d: d[c] = 0
        d[c] += sum
    keys = sorted(d)
    l = []
    for k in keys: l.append(k + ': ' + str(d[k]))
    print('\n'.join(l), end = '')

