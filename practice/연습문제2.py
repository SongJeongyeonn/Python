# 조건문, 반복문문
# 연습문제 1
fruit = ["사과", "포도", "홍시"]
user = (input("좋아하는 과일은?"))
if user in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

# 연습문제 2
주민등록번호 = (input("주민등록번호: "))
뒷자리 = 주민등록번호.split("-")[1]
if 0 <= int(뒷자리[1:3]) <= 8:
    print("서울 입니다.")
else:
    print("서울이 아닙니다.")
'''
requests.get을 사용해 변동폭 관련 가져올 수 있다.
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if(시가+변동폭) > 최고가:
    print("상승장", 시가, 최고가)
else:
    print("하락장")
'''

# 연습문제 3
add = 0
for i in range(1,11):
    add = add + i
print(add)

# 연습문제 4
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다."%(number+1))

# 연습문제 5
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end="")
    print('')

# 연습문제 6
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)
a = [1,2,3,4] # 리스트 컴프리헨션을 사용
result = [num * 3 for num in a]
print(result)
result = [num * 3 for num in a if num %2 == 0]
print(result)
result = [x*y for x in range(2,10) for y in range(1,10)]
print(result)

# 연습문제 7
list = ["SK하이닉스", "삼성전자", "LG전자"]
for i in range(0,3):
    print(len(list[i]))

# 연습문제 8
data = [[2000, 3050, 2050, 1980], [7500,2050,2050,1980],[15450,15050,15550,14900]]
for line in data:
    for j in line:
        print(j*1.0014)
result = []
sub = []
for line in data:
    for column in line:
        sub.append(column * 1.00014)
    result.append(sub)
print(result)

# 연습문제 9
ohlc = [["open", 'high', 'low', 'close'], [100,110,70,100],[200,210,180,190],300,310,300,310]
profit = 0
for row in ohlc[1:]:
    profit += (row[3] - row[0])
print(profit)