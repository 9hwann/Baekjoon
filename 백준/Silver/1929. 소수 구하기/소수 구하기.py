def decimal(num):
    if num == 1: return False
    if num == 2: return True
    else:
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
                break
        return True

import sys

m, n = map(int,sys.stdin.readline().split())

for i in range(m,n+1):
    if decimal(i):
        print(i)