kor = [70,60,55,75,95,90,80,80,85,100]
sum, i = 0, 0
while i < len(kor):
    sum += kor[i]
    i+=1
res = int(sum/(i+1))
print(res)