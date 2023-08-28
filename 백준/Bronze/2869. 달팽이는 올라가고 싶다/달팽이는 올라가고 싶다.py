a,b,v = map(int,input().split())

start = v // a
end = v // (a-b) + 1
day = 0

while start <= end:
    mid = (start+end) // 2

    if (mid-1) * (a-b) + a >= v:
        day = mid
        end = mid - 1

    else:
        start = mid + 1

print(day)