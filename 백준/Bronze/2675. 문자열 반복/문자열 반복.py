for _ in range(int(input())):
    n,a = input().split()
    n = int(n)
    b = ''

    for x in a:
        b += x*n

    print(b)