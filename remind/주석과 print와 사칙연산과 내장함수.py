# 이것은 주석입니다.
# 이 줄도 주석입니다.
# python은 c와 java에 비해 유저 친화적이다.

# print문
print("Hello, World!")
print(1+2) # 이렇게 숫자 바로 더함

# 사칙연산
print(32213 + 6243)
# 3
print(32213 - 6243)
# 38456
print(32213 / 6243) # java나 c와 다르게 소수점을 쭉 출력한다.
# 5.162162162162162
print(32213 * 6243)
# 201105759

# 변수 사용, 신기하게 앞에 타입 선언을 안한다. (들어오는 값을 보고 자동으로 타입이 지정됨)
a = 32213
b = 6243
print(a + b)
print(a - b)
print(a / b)
print(a * b)

a = 12
b = 56
print(a ** b) # 제곱연산
print(b % a) # 나머지 연산 이건 java와 같다.
print(b // a) # 이게 java의 /이다.

# 내장함수
# pow 함수:  거듭제곱(power)를 하겠다는 의미로, **과 같은 역할이다.
print( 3 ** 5 )
print( pow(3, 5) )
# 값이 243으로 똑같다.

print( pow(32555, 5242321223, 42) ) # 17
# 이게 바로 pow와 **의 차이점, 정수론에서 배우는 modular arithmetic을 구현 가능한데,
# **는 효율적인 알고리즘이 아니라 안되지만, 내장함수 pow를 사용하면 출력 가능

# divmod 함수: 몫과 나머지를 동시에 얻는 함수
# 기존 연산
a = 4096
b = 7
몫 = a // b
나머지 = a % b
print(몫)
print(나머지)
# divmod 연산
a = 4096
b = 7
몫, 나머지 = divmod(a, b)
print(몫)
print(나머지)

# math 내장라이브러리(built-in library): 제곱근, 로그, 삼각함수, 하이퍼볼릭함수, 360각도와 라디안의 변환, 최대공약수 구하기를 포함한 다양한 연산을 제공
import math

pi = math.pi # 원주율

print(math.sqrt(37)) # 37의 제곱근
print(math.isqrt(37)) # 37의 제곱근의 정수부분
print(math.ceil(37.5)) # 37.5의 ceiling function (주어진 수보다 작지않은 최소의 정수)
print(math.floor(37.5)) # 37.5의 floor function (주어진 수보다 크지 않은 최대의 정수)
print(math.sin(pi * 3 / 4)) # 4분의 3파이에 대한 sin 값
print(math.radians(60)) # 60도를 라디안으로 변환
print(math.cos(math.radians(75))) # cos 75도
