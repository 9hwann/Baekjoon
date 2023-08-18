n = int(input())
a = list(map(int,input().split()))

s = n

for i in range(n):
    if a[i] == 1:
        s -= 1
    else:
        for x in range(2,a[i]):
            if a[i] % x == 0 :
                s -= 1
                break

print(s)