n1 = int(input("첫번째 숫자 : "))
n2 = int(input("두번째 숫자 : "))
sansu = str(input("연산자 : "))
if sansu == '+':
     print(n1+n2)
elif sansu == '-':
     print(n1-n2)
elif sansu == '*':
     print(n1*n2)
elif sansu == '/':
    if n1 != 0 and n2 != 0:
         print(n1/n2)
    else:
        print("0으로 나눌수없습니다.")
else:
    print("+,-,*,/ 중 연산자를 입력해주세요")