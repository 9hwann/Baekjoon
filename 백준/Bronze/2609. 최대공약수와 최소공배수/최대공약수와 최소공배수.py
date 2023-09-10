def GCD(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def LCM(x,y):
    return x * y // GCD(x,y)

a, b = map(int,input().split())

print(GCD(a,b), LCM(a,b) ,sep='\n')