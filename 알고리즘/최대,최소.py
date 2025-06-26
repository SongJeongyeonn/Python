num = list(map(int, input().split()))
max = num[0]
for i in range(len(num)):
    if max < num[i]:
        max = num[i]
print(max)