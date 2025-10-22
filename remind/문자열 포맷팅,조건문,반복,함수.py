# 문자열 포맷팅

# c-style formatting (%를 사용해 포맷팅한다.)
print( "integer: %d, float: %.3f" % (3, 3.141592) )
print("pi: %.6f" % (3.141592653589793238) )
# 숫자 자리수를 제안하고 싶다면 %4.2f, %3d를 사용할 수 있다.
# 4.2f는 자리수가 4가 안되면 공백으로 채운 뒤, 소수점 2자리를 출력한다.

# curly bracket formatting
# c-style에서 %를 {}(placeholder)로 바꾸고, 뒤에 .format()을 붙여서 그 안에 값을 넣어준다.
print("I am {} and pi value is {}".format('developer', 3.141592653589793238))
# 소수점 자르기는 placeholder안에 조건을 적어 보여줄 수 있다.
print("The value of pi is {:.6f}".format(3.141592653589793238))
# curly bracket을 이용할 때의 장점은 placeholder에 이름을 붙이고, 그 위치마다 값을 넣어줄 수도 있다는 점이다.
print( "{이름}님의 잔고: 1억원, {이름}님의 은행은 {은행이름}입니다. {은행이름}의 서비스를 이용해주셔서 감사합니다 {이름} 고객님".format(이름='박재형', 은행이름='파이썬은행') )
# 이름을 지정한 상태에서 소수점 자르기도 가능하다
print("pi value = {pi:.3f}".format(pi=3.141592))
# s-style과는 다르게 list도 출력 가능하다
students = ['suzan', 'kevin', 'bob']
print("Students are {}".format(students))

# f-string
# 문자열을 생성하는 "이나 '' 앞에 f또는 F를 붙이는 것이다.
name = '박재형'
print( f"안녕하세요 {name} 고객님" )
# 소수점 자르기 (curly bracket과 유사)
pi = 3.14159265358979323238
print(f"pi = {pi:.3f}")
# 아래 코드는 글자 수를 제한하는 것을 제외하면, 위의 코드와 결과가 같다.
pi = 3.141592653589793238
print(f"{pi = }")
# 리스트나 다른 자료형도 가능하다
new_tuple = 1, 2, 3, 4
score = {"kevin": 10, "suzan": 3}
print(f"{new_tuple = }")
print(f"{score = }")

# boolean Type
print(1 == 1)
print(1 == 2)

# 조건문(if문)
# 단순히 true, false로
if True:
    print("Hello, True World!")
# 변수에 값을 넣어 변수의 true, false로
condition = False
if condition:
    print("Hello, True World!")
else:
    print("Hello, False World!")
# 변수 비교
score = 75
if score >= 90:
    print("Grade is A")
elif score >= 80:
    print("Grade is B")
else:
    print("Grade is C")

# 반복문
# for
print(1 + 5)
print(1 + 5)
print(2 + 5)
print(3 + 5)
print(5 + 5)
print(7 + 5)
print(12 + 5)
print(19 + 5)
# 이 과정을 for문을 사용하면 다음과 같이 바꿀 수 있다.
for i in [1, 1, 2, 3, 5, 7, 12, 19]:
    print(i + 5)
# while
a = 1
while a < 10:
    print(a)
    a += 2 
# 몫과 나머지를 구하는 코드
a = 65523
b = 37
q = 0
r = 0
while a >= b:
    a -= b
    q += 1
r = a
print(f"{q=} {r=}")

# 함수
def mul(_list):
    total = 1
    for i in _list:
        total *= i
    return total

print(mul([1, 2, 3, 5, 6, 7, 8, 10]))

# 재귀함수
def euclid(a:int, b:int) -> int:
    """
    두 양의 정수 a와 b의 최대공약수를 구하는 유클리드 호제법 알고리즘
    """
    q, r = divmod(a, b)
    if r == 0:
        return b
    return euclid(b, r)