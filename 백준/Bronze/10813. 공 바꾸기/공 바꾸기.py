n,m = map(int,input().split())
line = [i for i in range(1,n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    x = line[a-1]
    y = line[b-1]
    line[a-1] = y
    line[b-1] = x

for i in line:
    print(i,end=" ")