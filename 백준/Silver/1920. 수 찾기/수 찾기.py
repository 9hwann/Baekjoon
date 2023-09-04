from sys import stdin
from collections import Counter

N = stdin.readline()
n = list(map(int,stdin.readline().split()))
n_counter = Counter(n)

M = stdin.readline()
m = list(map(int,stdin.readline().split()))

for i in m:
    if n_counter[i] >= 1:
        print('1')
    else: print('0')