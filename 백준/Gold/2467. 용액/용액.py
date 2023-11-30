n = int(input())
solution = list(map(int,input().split()))
solution.sort()
left = 0
right = n-1
result = float('inf')
temp1 = 0
temp2 = 0

while left < right:
    temp = solution[left] + solution[right]
    if abs(temp) < result:
        result = abs(temp)
        temp1 = left
        temp2 = right
        if result == 0:
            break
    elif temp < 0:
        left += 1
    else:
        right -= 1

print(solution[temp1], solution[temp2])