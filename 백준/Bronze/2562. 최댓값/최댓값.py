x = 0
y = 0
count = 0

for i in range(1,10):
    a = int(input())
    y += 1
    if a > x:
        x = a
        count = y

print(x)
print(count)