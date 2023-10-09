import sys

n,m = map(int,sys.stdin.readline().split())
s = list(map(int,sys.stdin.readline().split()))
numbers = list(i for i in range(1,1002))

for q in s:
    numbers.remove(q)

result = float('inf')
for x in numbers:
    for y in numbers:
        for z in numbers:
            val = abs(n - x*y*z)
            result = min(result,val)
            if result == 0:
                break

print(result)