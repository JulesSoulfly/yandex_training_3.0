
# https://contest.yandex.ru/contest/45469/problems/16/
def e16():
    N, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b, queue = [], []
    for i in range(k):
        while len(queue) > 0 and queue[-1] > a[i]: queue.pop()
        queue.append(a[i])
    min = queue[0]
    b.append(str(min))
    if a[0] == min: queue.pop(0)

    first = 1
    for i in range(k, N):
        while len(queue) > 0 and queue[-1] > a[i]: queue.pop()
        queue.append(a[i])
        min = queue[0]
        b.append(str(min))
        if a[first] == min: queue.pop(0)
        first += 1
    print('\n'.join(b))


# https://contest.yandex.ru/contest/45469/problems/17/
def e17AAAAAAAAAAAA():
    N = int(input())
    b, queue = [], [0] * N
    start, end = 0, 0
    for i in range(N):
        l = input().split()
        if l[0] == '+':
            queue[end] = int(l[1])
            end += 1
        elif l[0] == '*':
            i = (end - start) // 2 + start + (end - start) % 2
            queue.insert(i, int(l[1]))
            end += 1
        elif l[0] == '-':
            b.append(str(queue[start]))
            start += 1
    print('\n'. join(b))


def e17():
    class lst:
        def __init__(self):
            self.first = None
            self.last = None
            self.mid = None
            self.len = 0

        def add(self, node, to_middle = False):
            if self.len == 0:
                self.first = self.mid = self.last = node
                self.len = 1
            else:
                if not to_middle:
                    self.last.next = node
                    self.last = node
                elif to_middle:
                    node.next = self.mid.next
                    self.mid.next = node
                    if self.len == 1: self.last = node
                self.len += 1
                if self.len == 2: self.mid = self.first
                elif self.len % 2 == 1: self.mid = self.mid.next

        def remove(self):
            a = self.first.n
            self.first = self.first.next
            self.len -= 1
            if self.len == 0:
                self.last = None
                self.mid = None
            else:
                if self.len in [1, 2]: self.mid = self.first
                elif self.len % 2 == 1: self.mid = self.mid.next
            return a

    class node:
        def __init__(self, n):
            self.n = n
            self.next = None

    N = int(input())
    a, b = lst(), []
    for i in range(N):
        l = input().split()
        if l[0] == '+': a.add(node(int(l[1])))
        elif l[0] == '*': a.add(node(int(l[1])), True)
        elif l[0] == '-': b.append(str(a.remove()))
    print('\n'. join(b))
