n,k = map(int,input().split())
a = list(map(int,input().split()))

if k > 1:
    for i in range(1,k):
        a.remove(max(a))

print(max(a))