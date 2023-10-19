n,m = map(int,input().split())
not_heard = set()
not_seen = set()

for _ in range(n):
    not_heard.add(input())
for _ in range(m):
    not_seen.add(input())

result = sorted(list(not_seen & not_heard))

print(len(result))
for x in result:
    print(x)