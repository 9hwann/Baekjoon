for _ in range(int(input())):
    a = int(input())
    b = int(input())
    floor = [i for i in range(1,b+1)]

    for i in range(a):
        temp = []
        for j in range(b):
            temp.append(sum(floor[:j+1]))
        floor = temp.copy()
    print(floor[-1])