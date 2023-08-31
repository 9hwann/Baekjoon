import sys
a = []

for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())

    if x == 0:
        a.pop()

    else:
        a.append(x)

print(sum(a))