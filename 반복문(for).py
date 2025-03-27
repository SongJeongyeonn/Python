# for 변수 in 리스트(또는 튜플, 문자열): 의 형태이다.

start = int(input("시작숫자를 입력하세요!:"))
end = int(input("끝 숫자를 입력하세요!:"))
_ = int(input("간격을 입력하세요!:"))
for i in range(start,end+1,_):
    print(i,end=" ")