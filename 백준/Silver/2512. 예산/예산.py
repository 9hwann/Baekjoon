n = int(input())
a = list(map(int,input().split()))
m = int(input())

left = 0
right = max(a)
result = 0

while left <= right:
    mid = (left+right) // 2
    temp = 0
    for i in a:
        if i <= mid:
            temp += i
        else:
            temp += mid

    if temp <= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)