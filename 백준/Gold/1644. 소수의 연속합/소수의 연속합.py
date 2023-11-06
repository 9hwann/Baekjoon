n = int(input())
a = [False,False] + [True] * (n-1)
decimal_list = []

for i in range(2,n+1):
    if a[i]:
        decimal_list.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

sum_decimal = [0]
s = 0
for k in decimal_list:
    s += k
    sum_decimal.append(s)

count = 0
left = 0
right = 0

while right <= len(sum_decimal)-1:
    if sum_decimal[right] - sum_decimal[left] == n:
        count += 1
        right += 1

    elif sum_decimal[right] - sum_decimal[left] > n:
        left += 1

    else:
        right += 1

print(count)