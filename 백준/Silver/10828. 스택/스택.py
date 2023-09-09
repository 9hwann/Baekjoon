import sys
from collections import deque
deq = deque([])

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        deq.appendleft(int(command[1]))
    elif command[0] == 'pop':
        if deq: print(deq.popleft())
        else: print(-1)
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        if not deq: print(1)
        else: print(0)
    elif command[0] == 'top':
        if deq: print(deq[0])
        else: print(-1)