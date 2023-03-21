
# https://contest.yandex.ru/contest/45469/problems/11/
def e11():
    n = int(input())
    aa, ans = [], []
    for _ in range(n): aa.append([float(x) for x in input().split()])
    for i in range(n):
        a = aa[i]
        if a[0] == 1: ans.append('1')
        else:
            st, b = [], []
            a.pop(0)
            while len(a) > 0:
                x = a.pop(0)
                if len(b) > 0 and b[-1] > x:
                    a.append(x)
                    break
                else:
                    while len(st) > 0 and x > st[-1]: b.append(st.pop())
                    st.append(x)
            if len(a) == 0: ans.append('1')
            else: ans.append('0')
    print('\n'.join(ans), end='')


# https://contest.yandex.ru/contest/45469/problems/12/
def e12():
    s = input().strip()
    exp, buf, bal, error = [], [], 0, 0
    b = {')': '(', ']': '[', '}': '{'}
    if len(s) == 0:
        print('WRONG')
    else:
        for c in s:
            if c == ' ':
                if len(buf) > 0: buf.append(' ')
            elif c == '(':
                if len(buf) > 0 or (len(exp) > 0 and (isinstance(exp[-1], int) or exp[-1] == ')')): # exp.append(int(''.join(buf)))
                    error = 1
                    break
                exp.append(c)
                bal += 1
            elif c == ')':
                if len(buf) > 0:
                    exp.append(int(''.join(buf)))
                    buf = []
                bal -= 1
                if bal < 0 or (not isinstance(exp[-1], int) and exp[-1] in '+-*('):
                    error = 1
                    break
                exp.append(c)
            elif c in '0123456789':
                if (len(buf) > 1 and buf[-1] == ' ') or (len(exp) > 0 and exp[-1] == ')'):
                    error = 1
                    break
                else: buf.append(c)
            elif c in '-+*':
                if len(buf) > 0:
                    exp.append(int(''.join(buf)))
                    buf = []
                if len(exp) == 0 or (not isinstance(exp[-1], int) and not exp[-1] == ')'):
                    error = 1
                    break
                exp.append(c)
            else:
                error = 1
                break
        if len(buf) > 0:
            exp.append(int(''.join(buf)))
            buf = []
        if len(exp) == 0 or (not isinstance(exp[-1], int) and exp[-1] in '-+*'): error = 1
        if error == 1 or bal != 0: print('WRONG')
        else:
            st = []
            for x in exp:
                if x == '(': st.append(x)
                elif x == ')':
                    o = st.pop()
                    while o != '(':
                        buf.append(o)
                        o = st.pop()
                elif x == '-' or x == '+':
                    while len(st) > 0 and st[-1] in '+-*': buf.append(st.pop())
                    st.append(x)
                elif x == '*':
                    while len(st) > 0 and st[-1] == '*': buf.append(st.pop())
                    st.append(x)
                else: buf.append(x)
            while len(st) > 0: buf.append(st.pop())
            for x in buf:
                if isinstance(x, int): st.append(x)
                else:
                    e2, e1 = st.pop(), st.pop()
                    if x == '+': st.append(e1 + e2)
                    elif x == '-': st.append(e1 - e2)
                    elif x == '*': st.append(e1 * e2)
            print(st[0])


# https://contest.yandex.ru/contest/45469/problems/13/
def e13():
    s = input().strip()
    st, buf = [], []
    for x in s:
        if x == '(':
            st.append(x)
        elif x == ')':
            o = st.pop()
            while o != '(':
                buf.append(o)
                o = st.pop()
            while len(st) > 0 and st[-1] == '!': buf.append(st.pop())
        elif x == '|' or x == '^':
            while len(st) > 0 and st[-1] in '|^&': buf.append(st.pop())
            st.append(x)
        elif x == '&':
            while len(st) > 0 and st[-1] in '&': buf.append(st.pop())
            st.append(x)
        elif x == '!':
            st.append(x)
        else:
            buf.append(x == '1')
            while len(st) > 0 and st[-1] == '!': buf.append(st.pop())
    while len(st) > 0: buf.append(st.pop())
    for x in buf:
        if x == True or x == False:
            st.append(x)
        else:
            e2 = st.pop()
            if x == '!':
                st.append(not e2)
            elif x == '^':
                e1 = st.pop()
                st.append(e1 ^ e2)
            elif x == '|':
                e1 = st.pop()
                st.append(e1 | e2)
            elif x == '&':
                e1 = st.pop()
                st.append(e1 & e2)
    print(int(st[0]))


# https://contest.yandex.ru/contest/45469/problems/14/
def e14():
    N, *a = [int(x) for x in input().split()]
    minL, minR, st, mx = [0]*N, [0]*N, [0], 0
    for i in range(1, N):
        while len(st) > 0 and a[st[-1]] > a[i]: minR[st.pop()] = i
        st.append(i)
    for i in range(len(st)): minR[st[i]] = N
    st = [N-1]
    for i in range(N-2, -1, -1):
        while len(st) > 0 and a[st[-1]] > a[i]: minL[st.pop()] = i
        st.append(i)
    for i in range(len(st)): minL[st[i]] = -1
    for i in range(N):
        mx = max(mx, (minR[i] - minL[i] - 1) * a[i])
    print(mx)


# https://contest.yandex.ru/contest/45469/problems/15/
def e15():
    s = input().strip('')
    if s[0] != '<':
        s[0] = '<'
        print(s)
    elif s[-1] != '>':
        s[-1] = '>'
        print(s)
    else:
        st, buf, isclose, i = [], [], False, 0
        for i in range(len(s)):
            c = s[i]
            if c == '<':
                if len(buf) == 0: buf.append(c)
            elif c == '/':
                if len(buf) == 1:
                    buf.append(c)
                    isclose = True
            elif c == '>':
                if len(buf) > 2:
                    buf.append(c)
                    if isclose:
                        pass

            else: buf.append(c)
