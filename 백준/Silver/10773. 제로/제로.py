a = []

for _ in range(int(input())):
    x = int(input())

    if x == 0:
        a.pop()

    else:
        a.append(x)

print(sum(a))