import sys

input = sys.stdin.readline

def add(p, x):
    if heap[p//2] > x:
        heap[p], heap[p//2] = heap[p//2], x
        add(p//2, x)

def delete(i):
    if len(heap) > i*2 and len(heap) > i*2+1:
        node = [heap[i*2], heap[i*2+1]]
        m = min(node)
        mi = i*2 if node.index(m) == 0 else i*2+1
        if heap[i] > m:
            heap[i], heap[mi] = m, heap[i]
            delete(mi)
        else:
            return
    elif len(heap) > i*2:
        if heap[i] > heap[i*2]:
            heap[i], heap[i*2] = heap[i*2], heap[i]
        else:
            return
    else:
        return
        
heap = [0]
p = 0
for i in range(int(input())):
    x = int(input())
    if x:
        p += 1
        heap.append(x)
        if p//2:
            add(p, x)
    else:
        if len(heap) == 1:
            print(0)
        elif len(heap) == 2:
            print(heap[1])
            heap.pop()
        else:
            print(heap[1])
            heap[1] = heap.pop()
            delete(1)
            p -= 1