n,m = map(int,input().split())

def fac(x):
    result = 1
    for i in range(1,x+1):
        result *= i
    return result

nCm = fac(n) // (fac(n-m) * fac(m))

print(int(nCm))