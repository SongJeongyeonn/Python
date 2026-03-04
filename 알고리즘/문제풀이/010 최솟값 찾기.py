from collections import deque
N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

# 새로운 값 삽입 시 정렬 대신 현재 수보다 큰 값 제거해 시간 복잡도 줄임.
for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i - L: # 범위에 벗어난 값 제거
        mydeque.popleft()
    print(mydeque[0][0], end=' ')