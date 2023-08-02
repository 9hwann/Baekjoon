n,m = map(int, input().split())
a = list()
b = list()

for a_row in range(0,n):
    a.append(list(map(int,input().split())))

for b_row in range(0,n):
    b.append(list(map(int,input().split())))

for x in range(0,n):
    for y in range(0,m):
        print(a[x][y] + b[x][y], end=" ")
    print('')