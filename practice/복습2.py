a = [1,2,3,1,2]
a.append(5)
print(a)
a.insert(3,6)
print(a)

c = [10,20,30]
c.remove(20) # 값을 기준으로 삭제
print(c)

c = [10,20,30]
del c[1]
print(c)

a = [1,2,3,4]
a.pop() # 4 제거 (제일 최근에 들어온 마지막 데이터 제거)
print(a)
a.pop(1) # 인덱스 1번 제거

a.clear # 전체 삭제
print(a)

for i in range(1,6): # 1~5까지 즉 6 미만
    print(i)

n = int(input("숫자를 입력해주세요:")) # 시험출제, 입력받은 자료형을 String이라 생각해 자료형 변환시키는 작업 꼭 필요
if n%2==0:
    print("짝수입니다")
else:
    print("홀수입니다")

# 계절 구하기
import datetime
now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print("현재는 봄 입니다.")
elif 6 <= month <= 8:
    print("현재는 여름 입니다.")
elif 9 <= month <= 11:
    print("현재는 가을입니다.")
else:
    print("현재는 겨울 입니다.")