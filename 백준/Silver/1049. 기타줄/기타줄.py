n, m = map(int,input().split())
pack_min = 1000
one_min = 1000

for _ in range(m):
    x, y = map(int,input().split())

    if x < pack_min:
        pack_min = x
    if y < one_min:
        one_min = y

if n <= 6:
    if pack_min < one_min * n:
        print(pack_min)
    else: print(one_min * n)

# 줄이 6개가 넘을 때 pack 가격이 낱개보다 싼 경우
elif pack_min < one_min * 6:
    pack = n // 6
    left = n % 6
    if pack_min < left * one_min:
        print((pack+1)*pack_min)
    else: print(pack*pack_min + left*one_min)

# 낱개가 더 싼 경우
else: print(n*one_min)