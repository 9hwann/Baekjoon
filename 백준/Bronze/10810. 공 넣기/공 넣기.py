n,m = map(int,input().split())
a = [0 for i in range(n)]


for i in range(m):
    x,y,z = map(int,input().split())
    a[x-1:y] = [z for i in range(y-x+1)]

for i in a:
    print(i, end=' ')