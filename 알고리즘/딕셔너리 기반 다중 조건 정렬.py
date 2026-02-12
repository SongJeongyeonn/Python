scores = [{'english': 80, 'math': 100},
          {'english': 100, 'math': 50},
          {'english': 70, 'math': 100},
          {'english': 80, 'math': 90}
          ]
# 수학↓, 수학이 같으면 영어 ↓
scores.sort(key=lambda x: ( -x['math'], -x['english'])) # 딕셔너리 키 사용.

for s in scores:
    print(s)