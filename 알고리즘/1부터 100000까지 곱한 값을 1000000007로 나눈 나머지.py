import time
answer = 1
start = time.time()
for i in range(1, 100001):
    answer *= i

result = answer % 1000000007 # 곱한 값을 1000000007로 나눈 나머지연산 수행하는 로직.
end = time.time()
print("결과:", result)
print("수행 시간: {:.6f}초".format(end - start))

# 수정 버전
MOD = 1000000007
answer = 1
start = time.time()
for i in range(1, 100001):
    answer = (answer * i) % MOD # 곱셈 수행 시 나머지 연산을 수행하는 로직 (바로 바로)

end = time.time()
print("결과:", answer)
print("수행 시간: {:.6f}초".format(end - start))

# 파이썬은 자동으로 형이 확장되어 정수 오버플로가 발생하지 않지만, 수가 커지면 연산 속도 자체가 느려질 수 있어, 중간 계산을 할 때마다 나머지 연산 적용하는 습관이 필요.