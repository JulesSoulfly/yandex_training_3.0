
# https://contest.yandex.ru/contest/45468/problems/11/
def e11():
    stack = []
    with open('input.txt', 'r') as f:
        while True:
            l = f.readline()
            if not l: break
            l = l.split()
            if l[0] == 'push':
                stack.append(int(l[1]))
                print('ok')
            elif l[0] == 'back':
                if len(stack) > 0:
                    print(stack[-1])
                else:
                    print('error')
            elif l[0] == 'pop':
                if len(stack) > 0:
                    print(stack.pop())
                else:
                    print('error')
            elif l[0] == 'size':
                print(len(stack))
            elif l[0] == 'clear':
                stack = []
                print('ok')
            elif l[0] == 'exit':
                print('bye')
                break


# https://contest.yandex.ru/contest/45468/problems/12/
def e12():
    s = input()
    st = []
    b = {')':'(', ']':'[', '}':'{'}
    mes = 'yes'
    for c in s:
        if c in '([{': st.append(c)
        else:
            if len(st) == 0 or st[-1] != b[c]:
                mes = 'no'
                break
            st.pop()
    if len(st) != 0: mes = 'no'
    print(mes)


# https://contest.yandex.ru/contest/45468/problems/13/
def e13():
    s = input().strip().split()
    st = []
    for c in s:
        if c == '-':
            x2 = st.pop()
            x1 = st.pop()
            st.append(x1 - x2)
        elif c == '+': st.append(st.pop() + st.pop())
        elif c == '*': st.append(st.pop() * st.pop())
        else: st.append(int(c))
    print(st[0])


# https://contest.yandex.ru/contest/45468/problems/14/
def e14():
    n = int(input())
    a = [int(x) for x in input().split()]
    st = []
    b = [0]
    for x in a:
        while len(st) > 0 and st[-1] - b[-1] == 1: b.append(st.pop())
        if x - b[-1] == 1: b.append(x)
        else: st.append(x)
    while len(st) > 0 and st[-1] - b[-1] == 1: b.append(st.pop())
    if len(b) == n+1: print('YES')
    else: print('NO')


# https://contest.yandex.ru/contest/45468/problems/15/
def e15():
    n = int(input())
    a = [int(x) for x in input().split()]
    st = [0]
    b = ["-1" for _ in range(n)]
    for i in range(1, n):
        while len(st) > 0 and a[st[-1]] > a[i]: b[st.pop()] = str(i)
        st.append(i)
    print(' '.join(b), end = '')
