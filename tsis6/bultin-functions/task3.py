str=input()
def ispali(str):
    if str==str[::-1]:
        return True
    else:
        return False
    
print(ispali(str))