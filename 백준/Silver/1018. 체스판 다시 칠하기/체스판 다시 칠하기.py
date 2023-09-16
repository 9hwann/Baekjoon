n,m = map(int,input().split())
a = []
count = []

for _ in range(n):
    a.append(input())

for i in range(n-7):
    for j in range(m-7):
        count_w = 0  # 시작지점이 W인 경우
        count_b = 0  # 시작지검이 B인 경우

        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y) % 2 == 0:
                    if a[x][y] != 'W': count_w += 1
                    else: count_b += 1
                else:
                    if a[x][y] != 'B': count_w += 1
                    else: count_b += 1
        count.append(min(count_w,count_b))

print(min(count))