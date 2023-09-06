n, k = map(int, input().split())

people = list(range(1, n + 1))
out = []
x = k - 1

while len(people) > 0:
    x %= len(people)
    out.append(people.pop(x))
    x += k - 1

print('<' ,end='')
print(', ' .join(map(str,out)) ,end='')
print('>')