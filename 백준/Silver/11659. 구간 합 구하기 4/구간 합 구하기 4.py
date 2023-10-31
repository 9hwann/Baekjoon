import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a = list(map(int,input().split()))

prefix_sum = [0]

temp = 0
for i in a:
    temp += i
    prefix_sum.append(temp)

for j in range(m):
    x,y = map(int,input().split())
    print(prefix_sum[y] - prefix_sum[x-1])