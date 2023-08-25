from sys import stdin

def binary_search(a, n, start, end):
    result = 0
    while start <= end:
        mid = (start+end) // 2
        count = 0

        for i in a:
            count += i // mid

        if count >= n:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

k, n = map(int,stdin.readline().split())
a = []

for _ in range(k):
    a.append(int(stdin.readline()))

print(binary_search(a, n, 1, max(a)))