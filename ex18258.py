import sys
from collections import deque
input  = sys.stdin.readline

num = int(input())
queue = deque([])

for i in range(num):
    msg = input().split()
    if msg[0] == 'push':
        queue.append(msg[1])
    elif msg[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif msg[0] == 'size':
        print(len(queue))
    elif msg[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif msg[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif msg[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
   
            