def checklen(pasw):
    return 32>=len(pasw)>=8

def checkstart(pasw):
    return pasw[0].isalpha()

def checkvalid(pasw):
    for letter in pasw:
        # print(letter)
        if letter in ['/',"\\","=","'",'"'," "]:
            return False
    
    return True
value = input()
print(checklen(value) and checkvalid(value) and checkstart(value))
