import sys

for _ in range(int(sys.stdin.readline())):
    n,m = map(int,sys.stdin.readline().split())
    line = list(map(int,sys.stdin.readline().split()))
    queue = []
    
    while list:
        m -= 1
        
        if line[0] == max(line):
            queue.append(line[0])
            del line[0]
            if m < 0:
                print(len(queue))
                break
        else:
            line.append(line[0])
            del line[0]
            if m < 0:
                m = len(line) - 1