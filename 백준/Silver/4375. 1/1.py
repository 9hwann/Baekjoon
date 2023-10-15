while True:
    try:
        n = int(input())
    except: break

    result = True
    temp = '1'

    while True:
        if int(temp) % n == 0:
            break
        else: temp += '1'

    print(len(temp))