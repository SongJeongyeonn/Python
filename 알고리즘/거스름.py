n, m = map(int, input().split())
coin = [0] * n
cnt = 0
for i in range(n):
    coin[i] = int(input())
for i in range(n - 1, -1, -1):
    if m >= coin[i]:
        cnt += m // coin[i]
        m = m % coin[i]

print(cnt)