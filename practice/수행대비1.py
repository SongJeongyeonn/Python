# 입력: python은 입력을 input()으로 받는다.
name = input("이름을 입력해주세요: ")
age = int(input("나이를 입력해주세요: ")) # input은 string 타입이기에 string이 아니면 해당 변수의 타입으로 감싸야함
print(f'당신의 이름은 {name}이며, 당신이 생일이 안 지났다면 만 {age-2}세압나다.')

# 자료형(int, float, str, bool, list, tuple, dict, set, None)
i: int = 4
ii = 4

f: float = 1.5
ff = 2.6

s: str = "안녕"
ss = "반가워!"

b:bool = 1
b = False

n = None

# 연속된 자료형

# 리스트: 순서 보장, 중복 허용, 수정 가능
list = [1,2,3,4,5]
list.append(6)
print(list)
list.pop()
list.insert(1,6)
print(list) 
list.remove(6)

doubleList = [[1,2,3],[4,5,6],[7,8,9]]
print(list+doubleList)
print(list[0:4], doubleList[0][0])

clist = ["ab", "cd", "de", "fg", "hi"]
clist[0] = clist[0].upper()
print(clist[0])

print("1~10까지 홀수만 저장한 리스트") # 좀 연습이 더 필요하다.
holelist = [a for a in range(1, 11, 2)]
print(holelist)

# 튜플
tuple = ('오예스', '몽쉘', '초코파이', '에이스')
a,b,*ex = tuple
print(ex)

# 세트
set = {1,2,3,4,5,5}
print(set) # 중복이 제거되어 나온다.
set.remove(2) 
set.discard(10)
print(set.pop())

# 딕셔너리
dict = {'one':1, 'two':2, 'three':3, 'five':4}
print(dict.pop('one'))
dict['one']  = 1
dict.update(five=5, four=4) # 추가와 수정 모두 가능
print(dict.popitem())
print(dict)

# 조건문
if i > f:
    print("i가 f보다 크다.")
elif i == f:
    print("i와 f가 같다.")
else:
    print("f가 i보다 크다.")

#반복문 (변수 초기화는 필수)
print("1부터 10까지 더하면?")
num = 0
for i in range(11):
    num += i
print(num)

while num > 0:
    num -= 5

print("1부터 100까지의 짝수만 더하면?")
for i in range(1, 101, 2):
    num += i
print(f'{num:,}') # ,는 천의 자리수를 나타냄

# 함수
def two(num):
    num *= num
    return num
num = int(input("제곱할 숫자를 입력하시오: "))
print(two(num))