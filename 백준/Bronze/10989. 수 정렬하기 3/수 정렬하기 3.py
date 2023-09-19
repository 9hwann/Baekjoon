import sys

a = [0 for i in range(10001)]

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a[n] += 1

for i in range(10001):
    if a[i] != 0:
        for _ in range(a[i]):
            print(i)