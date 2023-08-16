a = set()
for _ in range(int(input())):
    a.add(input())

a = list(a)
a.sort()
b = sorted(a, key = lambda x : len(x))

for i in b:
    print(i)