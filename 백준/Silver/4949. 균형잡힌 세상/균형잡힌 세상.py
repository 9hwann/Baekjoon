while True:
    ps = []
    a = input()

    if a == '.': break

    for i in a:
        if i == '(':
            ps.append(i)
        elif i == ')':
            if ps and ps[-1] == '(':
                ps.pop()
            else:
                ps.append(')')  # 여기서 print('NO')하면 이후 print 또 수행 -> a를 TRUE로 만들어 이후에 YES/NO 판단하게
                break
        elif i == '[':
            ps.append(i)
        elif i == ']':
            if ps and ps[-1] == '[':
                ps.pop()
            else:
                ps.append(']')
                break

    if ps: print('no')  # 연산 후 a가 비어있지 않으면 올바른 괄호 문자열 X
    else: print('yes')