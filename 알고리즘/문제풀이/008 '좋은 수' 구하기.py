import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
num.sort()
result = 0

for k in range(n): # 요소들 개수만큼 돌기
    find = num[k] # 첫 요소부터
    i = 0
    j = n-1
    while i < j:
        if num[i] + num[j] == find: # 서로 다른 수의 합인지
            if i != k and j != k: # 자기 자신 포함 X
                result += 1 # 경우 증가
                break
            elif i == k: # 이하 범위 조정
                i += 1
            elif j == k:
                j -= 1
        elif num[i] + num[j] < find: # 이하 범위 조정
                i += 1
        else:
                j -= 1
print(result) # 결과
