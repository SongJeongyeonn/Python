# n개의 숫자가 공백 없이 쓰여있을 때, 이 숫자를 모두 합해 출력하는 프로그램 작성.
n = input()
numbers = list(input())
result = 0
for i in numbers:
    result += int(i)
print(result)