# 오름차순 정렬: list.sort() vs sorted()
A = [5,3,2,4,1]

# 방법1: list.sort() - 리스트 자체를 정렬(in-place)
A.sort()  # sort() 오름차순 정렬
print("sort() 결과:", A)

A = [5,3,2,4,1]

# 방법2: sorted() - 정렬된 복사본을 반환(원본 변경 X)
B = sorted(A)  # sorted() 오름차순 정렬
print("원본 리스트:", A)
print("sorted() 결과:", B)

# list.sort()는 반환값 None, sorted(list)는 정렬된 복사본을 반환. (원본 필요 여부에 따라 적절한 방법 선택)

# 내림차순 정렬: reverse=True 옵션 사용 (위의 리스트 A가 초기화 상태이므로 초기화 코드 생략.)
A.sort(reverse=True)  # sort() 내림차순 정렬
print("내림차순 결과:", A)

B = sorted(A, reverse=True)  # sorted() 내림차순 정렬
print("내림차순 복사본:", B)

# python에서는 정렬함수를 직접 제어할 수 없는 경우도 존재한다.
A = [5,3,2,4,1]

# 부호 반전시키고 오름차순 정렬 후, 다시 부호 되돌리기.
A = [-x for x in A]  # 부호 반전
A.sort() 
A = [-x for x in A]  # 부호 되돌리기
print("부호 반전 후 내림차순 결과:", A)