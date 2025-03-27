# 리스트, 튜플 복습
# 연습문제 1
naver_closing_price = [488500, 500500, 501000, 461500, 474500]
print(naver_closing_price)
max_price = max(naver_closing_price)
print(max_price)
min_price = min(naver_closing_price)
print(min_price)
print(max_price-min_price)
print("수요일 종가: ", naver_closing_price[2])
naver_closing_price2 = {'09/11':488500, '09/10':500500, '09/09':501000, '09/08':461500, '09/07':474500}
print(naver_closing_price2['09/09'])