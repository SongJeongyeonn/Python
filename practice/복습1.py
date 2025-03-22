# type 함수로 자료형 확인
print(type("안녕"))
a = [4,2,7,3,5]
print(a[1:4:2])
print(a[-4:-1:2])
print(a[-4:4:2])
print(a[:4:2])
print(a[1:4])
print(a[1:])
print(a[1::2])
print(a[1:3:])
print(a[0:2]) # 2 미만 출력

print("----------------------------------")

del a[1]
print(a)
del a[0:2]
print(a)
print(len(a))
print(a.count(2)) # 해당 배열에서 2의 개수 (없으면 0)
a.append(5)
print(a)

a.sort() # 정렬 - 오름차순
print(a)
a.reverse()# 역순(그냥 뒤집기)
print(a)

a = [1, 2, 3, 1]
print(a.index(3)) # 인덱스 번호 반환
print(a.index(1)) # 중복일 경우 맨 앞에 있는 번호를 반환
print(min(a))
print(max(a))
print(sum(a))

# 튜플은 수정 시 불편