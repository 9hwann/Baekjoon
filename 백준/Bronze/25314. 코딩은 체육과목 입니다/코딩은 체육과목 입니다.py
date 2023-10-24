n = int(input())
if n % 4 == 0:
    x = n // 4
else:
    x = n // 4 + 1

for _ in range(x):
    print('long', end=' ')

print('int')