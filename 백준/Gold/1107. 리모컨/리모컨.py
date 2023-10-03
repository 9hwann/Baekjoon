import sys

n = int(sys.stdin.readline())
q = int(sys.stdin.readline())
broken = list(map(int,sys.stdin.readline().split()))

min_count = abs(n-100)

for i in range(1000001):
    for j in range(len(str(i))):
        if int(str(i)[j]) in broken:
            break
        elif j == len(str(i))-1:
            count = len(str(i)) + abs(i-n)
            min_count = min(min_count,count)

print(min_count)