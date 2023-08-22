a = input()

for i in range(1,int(a)+1):
    M = i

    for x in str(i):
        M += int(x)

    if M == int(a):
        print(i)
        break

    elif i == int(a):
        print('0')