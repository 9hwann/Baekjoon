import sys

m,n = map(int,sys.stdin.readline().split())
a = dict()

for i in range(1,m+1):
    x = sys.stdin.readline().rstrip()
    a[x] = i
    a[i] = x

for i in range(n):
    y = sys.stdin.readline().rstrip()
    try:
        z = int(y)
        print(a[z])
    except:
        print(a[y])