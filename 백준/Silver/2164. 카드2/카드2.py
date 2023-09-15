from collections import deque

a = deque(i for i in range(1,int(input())+1))

if len(a) == 1: print(1)

else:
    while len(a) > 2:
        a.popleft()
        a.append(a.popleft())

    a.popleft()
    print(a[0])