X = int(input())
N = int(input())
sum = 0

while N > 0:
    N -= 1
    a, b = map(int,input().split())
    sum += a*b

if X == sum:
    print("Yes")
else :
    print("No")