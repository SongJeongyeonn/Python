def pwd(pw):
    for h in range(0,10):
        for i in range(0,10):
            for j in range(0,10):
                for k in range(0,10):
                    made_pw = f'{h}{i}{j}{k}'
                    if str(pw) == made_pw:
                        print(made_pw)
                        return True
                    
print(pwd(3456))