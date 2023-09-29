n = int(input())
a = []
result = []

for _ in range(n):
    a.append(list(map(int,input().split())))

for i in a:
    count = 1

    for j in a:
        if i[0] < j[0] and i[1] < j[1]:
            count += 1

    result.append(count)

for x in result:
    print(x ,end=' ')