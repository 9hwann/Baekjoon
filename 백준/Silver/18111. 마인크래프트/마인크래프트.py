import sys

N,M,B = map(int,sys.stdin.readline().split())
a = []
time = int(1e9)
height = 0

for _ in range(N):
    line = list(map(int,sys.stdin.readline().split()))
    a.append(line)

for x in range(257):  # x : 목표 높이
    t = 0
    block_gain = 0
    block_use = 0

    for i in range(N):
        for j in range(M):
            if a[i][j] > x:
                block_gain += a[i][j] - x
            else:
                block_use += x - a[i][j]

    if block_use - block_gain <= B:
        t = block_gain * 2 + block_use

        if t <= time:
            time = t
            height = x

print(time, height)