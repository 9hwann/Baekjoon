n = int(input())
k = int(input())

start = 1
end = n * n

while start <= end:
    count = 0
    mid = (start+end) // 2

    for i in range(1,n+1):
        count += min(n, mid//i)

    if count >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)