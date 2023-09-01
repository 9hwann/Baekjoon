def factorial(num):
    result = num
    if num == 0:
        return 1
    else:
        for i in range(2,num):
            result *= i
        return result

import sys

n = int(sys.stdin.readline())
fac_n = str(factorial(n))
reverse_n = fac_n[::-1]

for i in range(len(fac_n)):
    if reverse_n[i] != '0':
        print(i)
        break