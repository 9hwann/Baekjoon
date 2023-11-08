n,s = map(int,input().split())
a = list(map(int,input().split()))

left,right = 0,0
total = 0
length = len(a) + 1

while True:
    if total >= s:
        length = min(length,right-left)
        total -= a[left]
        left += 1
    elif right == n:
        break
    else:
        total += a[right]
        right += 1

if length == len(a) + 1:
    print(0)
else:
    print(length)