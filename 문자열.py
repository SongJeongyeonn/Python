say = '"Python is very easy." he says'
print(say)
food = "Python\'s favorite food is perl"
print(food)
multiline="""...Life is too short
...You need python"""
print(multiline)

head = "Python"
tail = "is fun!"
print(head+tail)

a = "python"
print(a*2)

# multistring
print("=" * 50)
print("My Program")
print("=" * 50)

a = "Life is too short, You need Python"
print(len(a))
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0])
print(a[12])
print(a[-1]) # -1은 뒤에서부터 출력

# 문자열 슬라이싱
print(a[0:4])
print(a[19:])
print(a[19:-7])
print(a[:])

a = "Pithon"
# a[1] = 'y' 오류발생, 문자열의 요소 값은 바꿀 수 없기에

print(a[:1])
print(a[2:])
print(a[:1]+'y'+a[2:])

# 문자열 포매팅
print("I eat %d apples." %3)
print("I eat %s apples." %"five")
number = 3
print("I eat %d apples." %number)

number = 10
day = "three"
print("I ate %d apples, so I was sick for %s days." % (number, day))

print("Error is %d%%" % 98)

# 포맷함수 사용
print("I eat {0} apples".format(3))
number = 10
day = "three"
print("I eat {0} apples. so I was sick for {1} days.".format(number, day))
print("I eat {number} apples. so I was sick for {day} days.".format(number = 10, day = 3))

# 정렬과 공백
print("%10s" % "hi")
print("%-10sjane" % 'hi')

print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))

print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

y = 3.2124545
print("{0:0.4f}".format(y))

# f 문자열 포매팅
name = "홍길동"
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}이니다.')
print(f'나는 내년이면 {age + 1}살이 된다.')

print(f'{"hi":<10}')

print(f'난 {1500000:,}원이 필요해')

# 문자열 관련 함수들
a = "hobby"
print(a.count('b'))

a = "Python is the best choice"
print(a.find('b'))
print(a.find('k')) # 없으면 -1 반환
print(a.index('i'))

print(",".join('abcd'))

# join 함수의 입력으로 리스트를 사용하는 예
print(",".join(['a', 'b', 'c', 'd']))

a="hi"
print(a.upper())

a = "HI"
print(a.lower())

a = "  hi"
print(a.lstrip())

a = "   hi    "
print(a.strip())

a = "Life is too short"
print(a.replace("Life", "Your leg"))

print(a.split())
b = "a:b:c:d"
print(b.split(':'))