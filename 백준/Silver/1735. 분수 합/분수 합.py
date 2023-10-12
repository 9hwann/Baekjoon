def gcd(x,y):
    while x % y != 0:
        mod = x % y
        x = y
        y = mod
    return y


a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())

s2 = a2*b2
s1 = a1*b2 + b1*a2

g = gcd(s1,s2)
s1 = int(s1/g)
s2 = int(s2/g)

print(s1, s2)