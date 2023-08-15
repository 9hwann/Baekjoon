a=[]
for i in range(10):
    a.append(int(input())%42)

s = 0
for i in range(42):
    if a.count(i) > 0:
        s += 1

print(s)