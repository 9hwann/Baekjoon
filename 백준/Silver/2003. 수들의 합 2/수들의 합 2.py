n,m = map(int,input().split())
a = list(map(int,input().split()))

left = 0
right = 1
count = 0

while right <= n and left <= right:
    temp = a[left:right]
    temp_sum = sum(temp)

    if temp_sum == m:
        count += 1
        right += 1

    elif temp_sum < m:
        right += 1

    else :
        left += 1

print(count)