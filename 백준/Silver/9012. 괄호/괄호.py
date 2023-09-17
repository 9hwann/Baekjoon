for _ in range(int(input())):
    a = []
    ps = input()

    for i in ps:
        if i == '(':
            a.append(i)
        elif i == ')':
            if a:
                a.pop()
            else:
                a.append(')')
                break
    if a: print('NO')
    else: print('YES')

