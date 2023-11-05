n = int(input())
a = list(map(int,input().split()))
a.sort()
count = 0

for i in range(n):
    b = a[:]
    goal = b.pop(i)
    left = 0
    right = n-2

    while left < right:
        sum = b[left] + b[right]

        if sum == goal:
            count += 1
            break
        elif sum > goal:
            right -= 1
        else:
            left += 1

print(count)