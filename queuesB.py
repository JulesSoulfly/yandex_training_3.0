
# https://contest.yandex.ru/contest/45468/problems/16/
def e16():
    queue = []
    with open('input.txt', 'r') as f:
        while True:
            l = f.readline()
            if not l: break
            l = l.split()
            if l[0] == 'push':
                queue.append(int(l[1]))
                print('ok')
            elif l[0] == 'front':
                if len(queue) > 0:
                    print(queue[0])
                else:
                    print('error')
            elif l[0] == 'pop':
                if len(queue) > 0:
                    print(queue.pop(0))
                else:
                    print('error')
            elif l[0] == 'size':
                print(len(queue))
            elif l[0] == 'clear':
                queue = []
                print('ok')
            elif l[0] == 'exit':
                print('bye')
                break


# https://contest.yandex.ru/contest/45468/problems/17/
def e17():
    a1 = [int(x) for x in input().split()]
    a2 = [int(x) for x in input().split()]
    c = 0
    mes = 'botva'
    queue = []
    while c != 1000000 and len(a1) > 0 and len(a2) > 0:
        e1, e2 = a1[0], a2[0]
        if e1 == 9 and e2 == 0:
            a2.append(a1.pop(0))
            a2.append(a2.pop(0))
        elif e1 == 0 and e2 == 9:
            a1.append(a1.pop(0))
            a1.append(a2.pop(0))
        elif e1 < e2:
            a2.append(a1.pop(0))
            a2.append(a2.pop(0))
        elif e1 > e2:
            a1.append(a1.pop(0))
            a1.append(a2.pop(0))
        c += 1
    if len(a1) == 0: mes = 'second ' + str(c)
    elif len(a2) == 0: mes = 'first '  + str(c)
    print(mes)


# https://contest.yandex.ru/contest/45468/problems/18/
def e18():
    deque = []
    with open('input.txt', 'r') as f:
        while True:
            l = f.readline()
            if not l: break
            l = l.split()
            if l[0] == 'push_back':
                deque.append(int(l[1]))
                print('ok')
            elif l[0] == 'push_front':
                deque.insert(0, int(l[1]))
                print('ok')
            elif l[0] == 'front':
                if len(deque) > 0:
                    print(deque[0])
                else:
                    print('error')
            elif l[0] == 'back':
                    if len(deque) > 0:
                        print(deque[-1])
                    else:
                        print('error')
            elif l[0] == 'pop_front':
                if len(deque) > 0:
                    print(deque.pop(0))
                else:
                    print('error')
            elif l[0] == 'pop_back':
                if len(deque) > 0:
                    print(deque.pop())
                else:
                    print('error')
            elif l[0] == 'size':
                print(len(deque))
            elif l[0] == 'clear':
                deque = []
                print('ok')
            elif l[0] == 'exit':
                print('bye')
                break


# https://contest.yandex.ru/contest/45468/problems/19/
def e19():
    def insert(heap, x):
        heap.append(x)
        if len(heap) > 1:
            i = len(heap) - 1
            ii = (i - 1) // 2
            while i != 0 and heap[ii] < heap[i]:
                heap[ii], heap[i] = heap[i], heap[ii]
                i = ii
                ii = (i - 1) // 2
    def extract(heap):
        a = heap[0]
        if len(heap) == 1: heap.pop()
        elif len(heap) == 2: heap.pop(0)
        else:
            heap[0] = heap[-1]
            i = 0
            right = i*2+2
            while right < len(heap):
                if heap[right] > heap[i] and heap[right] >= heap[right-1]:
                    heap[right], heap[i] = heap[i], heap[right]
                    i = right
                elif heap[right-1] > heap[i] and heap[right-1] >= heap[right]:
                    heap[right-1], heap[i] = heap[i], heap[right-1]
                    i = right-1
                else: break
                right = i * 2 + 2
            heap.pop()
        return a
    heap, b = [], []
    n = int(input())
    for i in range(n):
        a = [int(x) for x in input().split()]
        if a[0] == 0: insert(heap, a[1])
        else: b.append(str(extract(heap)))
    #print(heap)
    print('\n'.join(b))


# https://contest.yandex.ru/contest/45468/problems/20/
def e20():
    N = int(input())
    a = [int(x) for x in input().split()]
    for j in range(N // 2, -1, -1):
        i = j
        left = i * 2 + 1
        while left < N:
            if left + 1 < N:
                if a[left] > a[i] and a[left] >= a[left + 1]:
                    a[left], a[i] = a[i], a[left]
                    i = left
                elif a[left + 1] > a[i] and a[left + 1] >= a[left]:
                    a[left + 1], a[i] = a[i], a[left + 1]
                    i = left + 1
                else:
                    break
            else:
                if a[left] > a[i]:
                    a[left], a[i] = a[i], a[left]
                    i = left
                else:
                    break
            left = i * 2 + 1
    max = N
    while max != 0:
        a[max-1], a[0] = a[0], a[max-1]
        max -= 1
        i = 0
        left = i * 2 + 1
        while left < max:
            if left + 1 < max:
                if a[left] > a[i] and a[left] >= a[left + 1]:
                    a[left], a[i] = a[i], a[left]
                    i = left
                elif a[left + 1] > a[i] and a[left + 1] >= a[left]:
                    a[left + 1], a[i] = a[i], a[left + 1]
                    i = left + 1
                else:
                    break
            else:
                if a[left] > a[i]:
                    a[left], a[i] = a[i], a[left]
                    i = left
                else:
                    break
            left = i * 2 + 1
    print(' '.join(str(x) for x in a))
