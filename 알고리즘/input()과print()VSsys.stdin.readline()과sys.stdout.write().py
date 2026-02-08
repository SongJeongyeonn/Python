a = int(input())
print(a)

# 데이터를 대량 처리 시 sys.stdin.readline()과 sys.stdout.write() 사용이 좋음.
import sys
b = int(sys.stdin.readline())
sys.stdout.write(str(b)+'\n') # sys.stdout.write는 문자열만 출력 가능하므로 str()로 변환 필요