n, m = map(int,input().split())
a = list(map(int,input().split()))

start = 1
end = max(a)

while start <= end:
    mid = (start+end) // 2
    len = 0

    for i in a:
        if i > mid:
            len += i - mid

    if len >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)