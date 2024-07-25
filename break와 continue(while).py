i = 0
while True:
    i+=1
    if i > 73:
        break
    if i % 10 != 3:
        continue
    print(i,end=' ')