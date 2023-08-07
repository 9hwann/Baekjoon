n = int(input())
x = 9

if n == 1:
    print(x)
else:
    for i in range(1,n):
        m = 4**i
        l = 2**(i)
        x = x + 5*m - (4*2+(l-2)*4*3+(l-2)*(l-2)*4)/2
    print(int(x))