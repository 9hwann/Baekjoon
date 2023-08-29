from sys import stdin
def round_all(num):
    num_int = int(num)
    if num - num_int >= 0.5:
        num_int += 1
    return(num_int)

n = int(stdin.readline())
a = []

if n == 0:
    print(0)

else:
    for _ in range(n):
        a.append(int(stdin.readline()))

    a.sort()
    cut = round_all(0.15*n)
    a = a[cut : n-cut]

    avg = sum(a) / len(a)
    print(round_all(avg))