import sys

n,m = map(int, sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

result = 0

for p in range(0,n):
    for q in range(p+1,n):
        for r in range(q+1,n):
            sum = a[p] + a[q] + a[r]

            if sum > result and sum <= m:
                result = sum

print(result)