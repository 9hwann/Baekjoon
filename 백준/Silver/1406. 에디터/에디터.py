import sys
from collections import  deque

input = sys.stdin.readline

left = deque(list(input().rstrip()))
right = deque([])

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'L':
        if left:
            right.appendleft(left.pop())

    elif command[0] == 'D':
        if right:
            left.append(right.popleft())

    elif command[0] == 'B':
        if left:
            left.pop()

    else:
        left.append(command[1])

x = list(left)
y = list(right)
print(''.join(x+y))