a = 1
aa = 1.0
print(a == aa) # 값만 본다.
print(a is aa) # 자료형을 본다.
aaa = input("1을 입력하시오.")
print(a,"는",aaa,"와 같은가?", a == aaa) # input으로 입력되는 값은 문자이다.
aaa = int(aaa) # int형으로 바꾼다.
print(a,"는",aaa,"와 같은가?", a == aaa)

print(max(2,6))
print(min(2,6))

print(type(6))
print(type(7.5))

a = 7
b = 3
c = a+b
print(type(c))
c = a/b
print(type(c))