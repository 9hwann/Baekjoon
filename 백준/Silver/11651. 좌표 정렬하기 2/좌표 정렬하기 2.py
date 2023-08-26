a = []
n = int(input())

for i in range(n):
    x,y = map(int,input().split())
    a.append([x,y])

a.sort(key = lambda x : (x[1],x[0]))

for i in range(n):
    print(a[i][0], a[i][1])