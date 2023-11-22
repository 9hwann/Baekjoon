n,m = map(int,input().split())
a = list(i for i in range(1,n+1))

for _ in range(m):
    x,y = map(int,input().split())
    temp = []
    for i in range(x-1,y):
        temp.append(a[i])
    for i in range(x-1,y):
        a[i] = temp[y-1-i]

for i in a:
    print(i, end=' ')