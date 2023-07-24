h, m = map(int,input().split())
t = int(input())

m = m + t

while m >= 60 :
    h += 1
    m -= 60

while h >= 24 :
    h -= 24

print(h, m)