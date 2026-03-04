import sys
input = sys.stdin.readline
n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum==n: # sum = n 라면 방법을 찾은거니까, count++해주고, end 올린다(현재 end에서 다른 start 값으로 sum이 될 수 없으니))
        count += 1
        end_index +=1
        sum += end_index
    elif sum > n: # 초과라면 start를 올려서 sum 감소한다
        sum -= start_index
        start_index +=1
    else: # 그외의 경우는 아직 수가 작으므로 end를 올려서 증가시킨다.
        end_index +=1
        sum += end_index
print(count)