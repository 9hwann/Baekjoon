n,k = map(int,input().split())
n_fac = 1
k_fac = 1

if k==1 or k==0:
    pass
else :
    for i in range(1,k+1):
        k_fac *= i

for i in range(n-k+1,n+1):
    n_fac *= i

print(int(n_fac/k_fac))