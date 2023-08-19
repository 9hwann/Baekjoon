while True:
    a = list(map(int,input().split()))
    if sum(a) == 0:
        break
    z = max(a)
    a.remove(max(a))
    x = a[0]
    y = a[1]
    if x**2 + y**2 == z**2:
        print("right")
    else:
        print("wrong")