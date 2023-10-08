n = int(input())
a = list(map(int,input().split()))
line = list(0 for _ in range(n))

for i in range(n):
    number = i+1
    order = a[i]
    count = 0
    x = 0
    while count < order:
        if line[x] == 0:
            x += 1
            count += 1
        else: x += 1

    while True:
        if line[x] == 0:
            line[x] = number
            break
        else:
            x += 1

for i in line:
    print(i, end=' ')