n = int(input())
x = n // 5

for i in reversed(range(x+1)):
    a = n - i*5
    if a % 3 == 0:
        print(i + a//3)
        break
    if i == 0:
        print(-1)