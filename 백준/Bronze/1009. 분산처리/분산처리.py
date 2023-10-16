for _ in range(int(input())):
    a,b = map(int,input().split())

    a = a % 10
    b = b % 4

    if b == 0:
        a = a ** 4
        while len(str(a)) > 1:
            a = a % 10
    else:
        a = a ** b
        while len(str(a)) > 1:
            a = a % 10

    if a == 0:
        print(10)
    else: print(a)