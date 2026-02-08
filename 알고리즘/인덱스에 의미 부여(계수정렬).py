import sys
N = int(sys.stdin.readline())
count = [0] * 1001 # 인덱스 숫자 자체
numbers = list(map(int, sys.stdin.readline().split()))

for num in numbers:
    count[num] += 1

for i in range(1001):
    if count[i] != 0:
        for _ in range(count[i]):
            sys.stdout.write(str(i) + ' ')

# 계수 정렬은 인덱스에 의미를 부여하는 대표적인 사례.