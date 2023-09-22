n = int(input())
x = 1
y = 6
count = 1

while x < n:
    x += y
    y += 6
    count += 1

print(count)