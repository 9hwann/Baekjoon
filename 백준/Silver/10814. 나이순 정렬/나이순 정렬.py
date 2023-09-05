from sys import stdin

n = int(stdin.readline())
a = []

for _ in range(n):
    x,y = stdin.readline().split()
    a.append((int(x),y))

a.sort(key = lambda x : x[0])

for i in range(n):
    print(a[i][0], a[i][1])