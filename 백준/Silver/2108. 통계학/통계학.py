def roundup_all(num):
    int_n = int(num)
    if num - int_n >= 0.5 :
        int_n += 1
    elif int_n - num >= 0.5:
        int_n -= 1
    return int_n

from sys import stdin
from collections import Counter

n = int(stdin.readline())
a = [int(stdin.readline()) for _ in range(n)]
a.sort()

arith = roundup_all(sum(a)/len(a))
mid = a[len(a)//2]
rng = max(a) - min(a)

b = Counter(a)
max_count = max(b.values())
mode_list = [num for num, freq in b.items() if freq == max_count]

if len(mode_list) > 1:
    mode_list.remove(min(mode_list))
    mode = min(mode_list)
else: mode = min(mode_list)

print(arith, mid, mode, rng ,sep='\n')