import sys
from collections import Counter

N = sys.stdin.readline()
n = list(map(int,sys.stdin.readline().split()))
n_counter = Counter(n)

M = sys.stdin.readline()
m = list(map(int,sys.stdin.readline().split()))

for i in m:
    print(n_counter[i] ,end=" ")