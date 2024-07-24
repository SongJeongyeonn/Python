n = int(input("목표 평균점수를 입력해주세요 : "))
e,m,c = map(float,input("영어, 수학, 컴시일의 점수를 입력해주세요 : ").split())
if 0 <= e <= 100 and 0 <= m <= 100 and 0 <= c <= 100:
    total = (e+m+c)/3
    if total >= n:
        print('목표 점수를 달성하셨습니다.')
    else:
        print('목표 점수를 달성하지 못했습니다.')
else:
    print("잘못된 입력입니다.")