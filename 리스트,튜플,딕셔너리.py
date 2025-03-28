# 리스트: 0개 이상의 요소를 가지며, 요소 추가, 삭제, 변경 가능
interest = ["삼성전자", "LG전자", "네이버"] #인덱스를 -1로 하면 거꾸로 접근한다.
print("기업: ", interest[0])

kospi_top10 = ['삼성전자', 'SK하이닉스', '현대차', '한국전력', '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명', 'NAVER', '현대모비스']
print(kospi_top10[0:5]) # 해당 인덱스 범위에 해당하는 요소가 출력된다. (슬라이스)
print(kospi_top10[5:10])
print(kospi_top10[5:-1])

print(kospi_top10[2:9:2]) # 세번째 숫자는 간격을 의미한다.

# 리스트의 몇 가지 연산
a = [1,2,3]
b = [5, 6]
c = a+b
print(c)
print(a*2)
print(a*0)

# d의 리스트에 3이 있니? in, not in 연산
d = [1,3,5,7,9]
print(3 in d)
print(3 not in d)

kospi_top11 = kospi_top10 # 원본 참조해서 11의 변화도 10에 반영된다.
kospi_top11.append('SK텔레콤')
print(kospi_top11)

kospi_top10.insert(3, 'SK텔레콤')
print(kospi_top10)

print(len(kospi_top10))

print(kospi_top10[-1])
del kospi_top10[-1]
print(kospi_top10)
print(len(kospi_top10))

b = a.copy()
a.clear()
print(a)
print(b)
a.extend([5,6,7,4])
print(a)
print(kospi_top10.index('현대차'))
a.sort()
print(a)

e = [1,2,'아',[1,2,3]] # 모든 타입의 데이터를 담을 수 있다. 리스트 안에 리스트도 담을 수 있다.
print(e)
print(e[3])
print(e[3][1]) # 리스트 안의 리스트 요소 프린트 가능

# 튜플: 리스트와 달리 변경이 불가하고(insert, append, del 조작 불가), ()로 감싸 만든다. (리스트와 유사) / 리스트보다 속도가 빠름
tu6 = (1, 2, 'apple')
print(tu6)
print(tu6[2])

#튜플 안의 리스트 요소를 변경하는 것은 가능하다.(하지만 리스트 전체는 수정 불가))
tu7 = (1, '아니', ['hi', 1, 2])
tu7[2][1] = 'ha'
print(tu7)

tu9 = (1, 2, 'banana', 'apple')
print(tu9[0])
print(tu9[-1])
print(tu9[1:])
print(tu9[1:3])
print(tu9[:-1]) # 끝에서 부터 마이너스 전까지

# 튜플의 연산
print(tu7+tu9)
print(tu7*2)
print(len(tu7))

animals = ('고양이', '사자')
scores = (65, 58, 12)
data = (animals, scores)
print(data)

# sort기능 없기에, 꼭 하고 싶다면 리스트로 변환하여 정렬해야한다.
tu10 = (4, 2, 3)
list_tu10 = list(tu10)
list_tu10.sort()
print(list_tu10)
tu11 = sorted(tu10)
print(tu11)

# 딕셔너리: 조사하는 단어를 key, 그 값을 value{}로 key와 value를 지정해서 만든다. (단어:설명이 쌍으로 이루어진 자료구조이다.)
str_duct = {'s':'study', 'p':'python', 'e':'easy'} # key 값은 유일함으로 여러개가 존재할 수 없다.
print(str_duct)
str_ductm = {'s':'study', 'p':'python', 'e':'easy', 'e':'elearing'} # 하나의 키에 여러 개의 값은 존재할 수 있다.
str_duct = {'s':'study', 'p':'python', 'e':['easy','elearing']} # key값을 여러개 넣을려면 리스트로 감싸주면된다.

# 인덱싱 순서와 슬라이스 못 사용, 인덱싱이 숫자가 아니라 key 값이기 때문
dict1 = {} # 빈 딕셔너리
dict2 = dict([(1, 'one'), (2, 'two')])
dict3 = {'one':1, 'two':2}
dict4 = dict(one=1, two=2)
dict5 = {1:['일','one'], 2:['이','two'], 3:['삼','three']}

print(dict2[1])
print(dict4['one'])

# 기본연산 (키 인덱싱을 활용하여 추가)
dict={1:'one', 2:'two', 3:'three'}
dict[0] = 'zero'
print(dict)

del dict[3]
print(dict)

# 응용 메소드
print(dict.get(1))
print(dict.get(3,'Upps..')) # 없을 시 'Upps..' 출력

print(dict.pop(1))
print(dict.pop(1,'Uppps')) # 없을 시 'Upps..' 출력

# 인덱스 위치 다루기
a = [1,2,3,4,1]
first = a.index(1)
second = a.index(1, first + 1)
print("첫 번째 1의 위치:", first)
print("두 번째 1의 위치:", second)