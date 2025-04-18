# 1부터 10까지의 숫자 중 짝수만 리스트로 만들기
list1 = [a for a in range(1, 11) if a % 2 == 0] # range 범위 잘 잡기!! range(초깃값, 범위, 건너뛸 수)
print(list1)
# 주워진 문자열 리스트에서 길이가 3 이상인 문자열만 골라 리스트 만들기
words = ['hi', 'sun', 'go', 'apple', 'on']
list2 = [words[a] for a in range(len(words)) if len(words[a]) >= 3] # len()이 길이 함수수
print(list2)

'''
list2 = [word for word in words if len(word) >= 3] 이게 더 간결하다..

'''
# 리스트에 있는 숫자를 모두 제곱하여 새로운 리스트 만들기
nums = [1, 2, 3, 4]
list3 = [num*num for num in nums]
print(list3)
# 음수만 골라 리스트 만들기
nums = [3, -1, 0, -7, 8, -2]
list4 = [n for n in nums if n < 0]
print(list4)
# 1부터 10까지 숫자 중 3의 배수만 문자열로 바꾸어 리스트 만들기
list5 = [str(a) for a in range(1,11) if a % 3 == 0]
print(list5)
# 주워진 문자열 리스트에서 모두 대문자로 바꿔 새로운 리스트 만들기
words = ['hello', 'bye', 'Good']
list6 = [word.upper() for word in words] # 인덱스를 가져오는게 아니라 값을 가져오는거다..
print(list6)
# 주어진 숫자 리스트에서 짝수는 그대로, 홀수는 -1로 바꿔서 리스트 만들기
nums = [1, 2, 3, 4, 5]
list7 = [n if n % 2 == 0 else -1 for n in nums] # 조건이 결과에 영향을 줄 땐 이렇게, 조건이 필터 역할만 할 땐 반대로
print(list7)

a = [1,2,3,4,5]
b = [6,7,8,9]
a.extend(b)
print(a)
print(a+b)

print(f'{"hi":<10}')

jk = [2,1,68,53]
jk.sort()
jk.reverse()
print(jk)

af = 'av'
af.upper()
print(af.upper())

a = input()
print(type(a))