while True:
    a = list(input())
    b = list(reversed(a))

    if a == ['0']:
        break
    elif a == b:
        print('yes')
    else :
        print('no')